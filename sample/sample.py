import sys


sys.path.append("/home/mohansai/python/Python_adb/M_adb")
import myadb


def main():
    #print(myadb.hellow())
    adb = myadb.madb()

    #adb._data_()
    #adb.run_cmd()
    adb.adb_devices()


if __name__ == "__main__":
    main()