#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import signal
import sys
import threading

def handleKill(signum, frame):
    print("Killing Thread.")
    # 必要に応じて終了前の処理を追加
    print(threading.active_count())
    sys.exit(0)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_highlight_finder.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    


if __name__ == "__main__":
    # シグナルハンドラの登録
    signal.signal(signal.SIGINT, handleKill)
    signal.signal(signal.SIGTERM, handleKill)

    # 以下のコードは、デフォルトのDjangoのmanage.pyの内容です。
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yt_highlight_finder.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
