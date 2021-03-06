# PythonTools
自分用のPython便利ツール

## Description

### Design
設計のためのツール群

### Timer
時間計測ツール群

## How to install
```bash
pipenv install git+https://github.com/mdonaka/MyPythonTools.git#egg=mypythontools
```

## How to use

### Design.Singleton
クラスに継承するだけでSingletonクラスになる．
```Python
from mypythontools.Design import Singleton

# Singleton class 
class A(Singleton): ...

# not Singleton class
class B: ...
```

### Design.i
iteratorをメソッドチェーンができるように拡張する．
```Python
from mypythontools.Design import i

itr = i([1,2,3,4,5])
newList = itr.map(lambda x:x+10).reverse().to_list()
print(newList) #output: "[11, 12, 13, 14, 15]"
```

### Timer.stop_watch
関数にデコレートするだけで処理時間を計測する．ログレベルは"DEBUG"としている．
```Python
from logging import DEBUG, basicConfig
from mypythontools.Timer import stop_watch
basicConfig(level=DEBUG)

@stop_watch
def func(): ...

func() #output: "DEBUG:[func_name] took [time] ms"
```
