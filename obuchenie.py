import logging

logging.basicConfig(level=10)
a_log=logging.getLogger()
print(a_log)

ch=logging.StreamHandler()
ch.setLevel(30)
a_log.addHandler(ch)
a_log.warning('jklo')

print(a_log.handlers)