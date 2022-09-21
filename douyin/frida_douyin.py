import frida
import sys
import time

device = frida.get_remote_device()
app_package_name = "com.youku.phone"
pid = device.spawn([app_package_name])

device.resume(pid)
time.sleep(1)

session = device.attach(app_package_name)


scr = """
Java.perform(function () {
    
	var Builder = Java.use("okhttp3.o$a");
     send('fund OkHttpClient$Builder success !!!'+Builder);
     Builder.b.overload("java.net.Proxy").implementation = function(){
        send('arg-' + arguments[0])
        var InetSocketAddress = Java.use("java.net.InetSocketAddress")
        var Proxy = Java.use("java.net.Proxy")
        var addr = InetSocketAddress.$new("10.100.50.33",8888)
        var Type = Java.use("java.net.Proxy$Type")
        var ppp = [];
        ppp.push( Proxy.$new(Type.HTTP.value,addr))
        var ret = this.b.apply(this, ppp);
        console.log("result "+ret);
        return ret;
    };
    
    
    var automock_b = Java.use("com.youku.phone.tools.automock.b");
        automock_b.b.overload('java.lang.String','okhttp3.Callback').implementation = function(){
        send('automock_b arg-' + arguments[0])
        var ret = this.a.apply(this,arguments);
        return ret;
    }
    
    
    var RouteSelector = Java.use("okhttp3.internal.connection.RouteSelector");
    
    RouteSelector.a.overload("okhttp3.HttpUrl",'java.net.Proxy').implementation = function(){
        send('RouteSelector arg-' + arguments[0])
        var InetSocketAddress = Java.use("java.net.InetSocketAddress")
        var Proxy = Java.use("java.net.Proxy")
        var addr = InetSocketAddress.$new("10.100.50.33",8888)
        var Type = Java.use("java.net.Proxy$Type")
        arguments[1] = Proxy.$new(Type.HTTP.value,addr)
        var ret = this.a.apply(this,arguments);
        console.log("result "+ret);
    };





    send('fund OkHttpClient$Builder success !!!')
	var d = Java.use("mtopsdk.mtop.global.d");
    send('fund class success !!!'+d);
    d.TD.overload('boolean').implementation = function(){
        send('classTD arg-' + arguments[0])
        arguments[0] = false;
        var ret = this.TD(arguments);
        
        return ret;
    };
    d.TE.overload('boolean').implementation = function(){
        send('classTE arg-' + arguments[0])
        arguments[0] = false;
        var ret = this.TE(arguments);
        
        return ret;
    };
});
"""



script = session.create_script(scr)
def on_message(message,data):
	print (message)
script.on("message",on_message)
script.load()
sys.stdin.read()



