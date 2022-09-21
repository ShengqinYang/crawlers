// Java.perform(function () {
//     console.log('ksishi')
//     var encrypt = Java.use("com.luojilab.netsupport.utils.a");  //对象名
//     //其中a为方法名,overload为重加载 ,"android.content.Context", "java.util.Map"为方法入参的数据类型
//     encrypt.a.overload("okhttp3.Request", "java.lang.String").implementation = function(args, args2) {
//         // console.log('a2', a2)
//         console.log("参数1", args)
//         console.log("参数2", args2)
//         var result = this.a(args, args2)
//         console.log("结果", result)
//         return result
//     }
// });

//参数1 Request{method=POST, url=https://entree.igetget.com/label/navigation/content, tags={class retrofit2.Invocation=com.luojilab.netsupport.netcore.builder.EmbedApiService.RetrofitPostFormApi() [https://entree.igetget.com/label/navigation/content, {page_id=0, result_type=0, product_type=2, navigation_id=61, h={"u":"267241698","thumb":"xl","dt":"phone","ov":"9","net":"wifi","os":"ANDROID","d":"07eb81a017fe33d5","dv":"MI 5","t":"json","chil":"1","v":"2","av":"8.5.0","scr":"3.0","adv":"1","ts":"1600674000","s":"7fdcab3b5d99f1d8","seid":"07eb81a017fe33d5"}, type=1, request_id=0, label_id=0, is_login=0, page_size=20, relation_id=61}, {}]}}
// 参数2
// 结果 Request{method=POST, url=https://entree.igetget.com/label/navigation/content, tags={class retrofit2.Invocation=com.luojilab.netsupport.netcore.builder.EmbedApiService.RetrofitPostFormApi() [https://entree.igetget.com/label/navigation/content, {page_id=0, result_type=0, product_type=2, navigation_id=61, h={"u":"267241698","thumb":"xl","dt":"phone","ov":"9","net":"wifi","os":"ANDROID","d":"07eb81a017fe33d5","dv":"MI 5","t":"json","chil":"1","v":"2","av":"8.5.0","scr":"3.0","adv":"1","ts":"1600674000","s":"7fdcab3b5d99f1d8","seid":"07eb81a017fe33d5"}, type=1, request_id=0, label_id=0, is_login=0, page_size=20, relation_id=61}, {}]}}
//a(String str, String str2, String str3, String str4, String str5, String str6, String str7, String str8, long j)
// Java.perform(function () {
//     console.log('ksishi')
//     var encrypt = Java.use("com.luojilab.netsupport.utils.a");  //对象名
//     //其中a为方法名,overload为重加载 ,"android.content.Context", "java.util.Map"为方法入参的数据类型
//     encrypt.a.overload("java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String",
//         "java.lang.String", "java.lang.String", "java.lang.String", "java.lang.String", "long").implementation = function (args1, args2, args3, args4, args5, args6, args7, args8, args9) {
//         // console.log('a2', a2)
//         console.log("参数1", args1)
//         console.log("参数2", args2)
//         console.log("参数3", args3)
//         console.log("参数4", args4)
//         console.log("参数5", args5)
//         console.log("参数6", args6)
//         console.log("参数7", args7)
//         console.log("参数8", args8)
//         console.log("参数9", args9)
//         var result = this.a(args1, args2, args3, args4, args5, args6, args7, args8, args9)
//         console.log("结果", result)
//         console.log('------------------')
//         return result
//     }
// });

//参数1 /label/navigation/content
// 参数2 POST
// 参数3
// 参数4 application/x-www-form-urlencoded
// 参数5 page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61

// 参数6 1600679506 --G-Auth-Ts 时间戳 2020-09-21 17:11:46
// 参数7 13a7105f62c650eaada4e9795a3c5c96  --G-Auth-Nonce

// --  G-Auth-Token
// 参数8 eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA
// 参数9 267241698  --userid u 固定值
// 结果 cf4338503bfa49e0902fa4ca7c6159b08c386749   --G-Auth-Sign


// 463ceba202a9f6f9ac4cd98d0f2f2876204ea85c  --G-Auth-Appid
//
Java.perform(function () {
    console.log('ksishi')
    var encrypt = Java.use("com.luojilab.b.d.a");  //对象名
    //其中a为方法名,overload为重加载 ,"android.content.Context", "java.util.Map"为方法入参的数据类型
    encrypt.a.overload("java.lang.String").implementation = function (args) {
        // console.log('a2', a2)
        console.log("参数1", args, typeof result)
        var result = this.a(args)
        console.log("结果", result, typeof result)
        return result
    }
});
// com.luojilab.b.d.a.a("android" + userId + DeviceUtils.getDeviceId(BaseApplication.getAppContext()) + c());
// 参数1 android 267241698 07eb81a017fe33d5  1600683246 052841885 纳秒
// 结果 326a30e6bb6f81c6597613d32bf5d95b

// page_id=0&result_type=0&product_type=2&navigation_id=61&h={"u":"267241698","thumb":"xl","dt":"phone","ov":"9","net":"wifi","os":"ANDROID","d":"07eb81a017fe33d5","dv":"MI 5","t":"json","chil":"1","v":"2","av":"8.5.0","scr":"3.0","adv":"1","ts":"1600679506","s":"7fdcab3b5d99f1d8","seid":"07eb81a017fe33d5"}&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61


// 参数1 android26724169807eb81a017fe33d51600741335863898565 undefined
// 结果 bd04cef92e993609b33d056df82a4380 string