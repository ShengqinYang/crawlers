console.log("[*]  Java Starting script");

rpc.exports = {
    "myfunc": function (qidian_url, method, requestbody) {
        var result = {};
        Java.perform(function () {
            // var qidian_url = "https://druidv6.if.qidian.com/argus/api/v1/bookstore/getbooks?pageIndex=1&pageSize=20&siteId=12&filters=&order=11";
            // var method = "GET";
            var tt1 = Java.use("com.qidian_app.QDReader.QDApplication").$new();
            var ret = tt1.a(qidian_url, method, requestbody);
            result['QDSign'] = ret.get("QDSign").toString();
            result['QDInfo'] = ret.get("QDInfo").toString();
            result['AegisSign'] = ret.get("AegisSign").toString();
            result['Cookie'] = ret.get("Cookie").toString();
            result['User-Agent'] = ret.get("User-Agent").toString();
            console.log(JSON.stringifyaa(result)); //将json转字符串
        });
        return result
        // return JSON.stringify(result)
    }
};