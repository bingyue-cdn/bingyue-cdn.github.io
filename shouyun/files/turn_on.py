from nonebot.log import logger
import httpx

verison = "0.1" # 版本信息
mirr = "cdn.bingyue.top" # 更新源
# 另外的更新源 blog.bingyue.top

logger.success("兽云nonebot2 插件启动成功")
logger.success("当前版本为0.1 beta测试版")
logger.success("如有问题可以来https://github.com/bingqiu456/shouyun 来反馈")
logger.warning("正在检查更新，请勿退出")

a = httpx.get(url=f"https://{mirr}/shouyun/1.json").json()
if a["ver"] == verison:
    logger.success("暂无新版本更新")
else:
    logger.warning(f"检测到新版本:{a['ver']}\n更新日志\n{a['log']}")
    logger.success(f"正在为你下载更新")
    for i in a["files"]:
        n = httpx.get(url=f"https://{mirr}/shouyun/files/{i}").text
        with open(f"plugins/{i}") as f:
            f.write(n)
            f.close()
        logger.success("正在下载最新版")

logger.success(" ╰(*°▽*)╯ 祝你使用愉快")