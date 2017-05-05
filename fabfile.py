from fabric.api import local

def test():
  local("cd /opt/fabtest/sss && touch file1 file2 file3")
  local("cd /opt/fabtest/sss && git add . && git commit -m test")
  local("cd /opt/fabtest/sss && git push origin master")

