import frida
import sys


def on_message(message, data):
    print("[%s] => %s" % (message, data))


def start_hook():
    device = frida.get_remote_device()
    print(device)
    # 应用包名
    app_package_name = "cn.missfresh.application"
    # app_package_name = "com.qidian_app.QDReader" # 抖音极速
    # try:
    # processes = device.enumerate_processes()
    # for process in processes:
    #     print(process)


    # session = device.attach(app_package_name)
    # modules = session.enumerate_modules()
    # for module in modules:
    #     print(module)
        # export_funcs = module.enumerate_exports()
        # print("\tfunc_name\tRVA")
        # for export_func in export_funcs:
        #     print("\t%s\t%s" % (export_func.name, hex(export_func.relative_address)))

    # 方案一
    pid = device.spawn([app_package_name])
    session = device.attach(pid)
    device.resume(pid)
    print("[*] start hook")
    print(session)

    # 加载脚本
    with open("hook_meiriyouxian.js", "r", encoding="utf-8") as file:
        js_code = file.read()

    script = session.create_script(js_code)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()  # 等待程序触发,调试时打开
    # return script
    # except frida.NotSupportedError:
    #     print("请检查包名的有效性.")


if __name__ == '__main__':
    start_hook()
