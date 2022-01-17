import logging
from logging.handlers import RotatingFileHandler
import datetime
print(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
}


def UseStyle(string, mode = '', fore = '', back = ''):

    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].get(mode) else ''

    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].get(fore) else ''

    back  = '%s' % STYLE['back'][back] if STYLE['back'].get(back) else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end   = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, string, end)


'''
debug：最细微的信息记录到debug中，这个级别就是用来debug的，看程序在哪一次迭代中发生了错误，比如每次循环都输出一些东西用debug级别
info：级别用于routines，也就是输出start finish 状态改变等信息
warn：输出一些相对重要，但是不是程序bug的信息，比如输入了错误的密码，或者连接较慢
error：输出程序bug，打印异常信息
critical：用于处理一些非常糟糕的事情，比如内存溢出、磁盘已满，这个一般较少使用
'''
class Logger:
    def __init__(self,inLevel='DEBUG',inName=__name__):
        self.logger = logging.getLogger(inName)
        self.logger.setLevel(inLevel)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def addHand(self,source):
        self.logger.addHandler(source)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)#

    def critical(self, msg):
        self.logger.critical(msg)

class FileLogger(Logger):#log文件输出类

    def __init__(self, logName):
        Logger.__init__(self, inLevel='DEBUG', inName=__name__)
        self.loggerName = logName
        self.rHandler = RotatingFileHandler("{}_{}.log".format(self.loggerName,datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')),maxBytes = 1*1024,backupCount = 3,encoding='utf-8')
        self.rHandler.setFormatter(self.formatter)
        self.addHand(self.rHandler)

class ConsoleLogger(Logger):#控制台输出日志类

    def __init__(self):
        Logger.__init__(self, inLevel='DEBUG', inName=__name__)
        self.console = logging.StreamHandler()
        self.console.setFormatter(self.formatter)
        self.addHand(self.console)
    def debug(self, msg):
        self.logger.debug(UseStyle(msg, fore = 'black'))#黑色

    def info(self, msg):
        self.logger.info(UseStyle(msg, fore = 'blue'))#蓝色

    def warning(self, msg):
        self.logger.warning(UseStyle(msg, fore = 'yellow'))#黄色

    def error(self, msg):
        self.logger.error(UseStyle(msg, fore = 'red'))#红色

    def critical(self, msg):
        self.logger.critical(UseStyle(msg, fore = 'purple'))#紫红色



log = ConsoleLogger()#控制台日志
#log = FileLogger('songqin_vip_xt')#文件日志
log.debug('调试')
log.info('信息')
log.warning('警告')
log.error('错误')
log.critical('糟糕')
