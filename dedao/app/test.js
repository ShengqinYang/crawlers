console.log("[*]  Java Starting script");

rpc.exports = {
    "myfunc": function (args1, args2, args3, args4, args5, args6, args7, args8, args9) {
        // console.log(args1, args2)
        var ret = {}
        Java.perform(function () {
            var tt1 = Java.use("com.luojilab.netsupport.utils.a")
            // var args1 = "/label/navigation/content";
            // var args2 = "POST";
            // var args3 = "";
            // var args4 = "application/x-www-form-urlencoded";
            // var args5 = "page_id=0&result_type=0&product_type=2&navigation_id=61&h=%7B%22u%22%3A%22267241698%22%2C%22thumb%22%3A%22xl%22%2C%22dt%22%3A%22phone%22%2C%22ov%22%3A%229%22%2C%22net%22%3A%22wifi%22%2C%22os%22%3A%22ANDROID%22%2C%22d%22%3A%2207eb81a017fe33d5%22%2C%22dv%22%3A%22MI%205%22%2C%22t%22%3A%22json%22%2C%22chil%22%3A%221%22%2C%22v%22%3A%222%22%2C%22av%22%3A%228.5.0%22%2C%22scr%22%3A%223.0%22%2C%22adv%22%3A%221%22%2C%22ts%22%3A%221600679506%22%2C%22s%22%3A%227fdcab3b5d99f1d8%22%2C%22seid%22%3A%2207eb81a017fe33d5%22%7D&type=1&request_id=0&label_id=0&is_login=0&page_size=20&relation_id=61";
            // var args6 = "1600741335";
            // var args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzI3MDQyNSwiaWF0IjoxNjAwNjc4NDI1LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNjc4NDI1LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.BlHdE91DxtsuUxjlDApbr9ArVB_Rb55vqZUCw5Nn7kFUpgEV1nKAEbkKWYu8Wzgucxvj6AVB-aGnkGsDH6j9PA";
            // // var args8 = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJpZ2V0Z2V0LmNvbSIsImV4cCI6MTYwMzM0MTQxOSwiaWF0IjoxNjAwNzQ5NDE5LCJpc3MiOiJEREdXIEpXVCBNSURETEVXQVJFIiwibmJmIjoxNjAwNzQ5NDE5LCJzdWIiOiIyNjcyNDE2OTgiLCJkZXZpY2VfaWQiOiIiLCJkZXZpY2VfdHlwZSI6IiJ9.O3Waka6SOxqfRp0bMn5zx6HehgcHys3BkxWXQpLm3Di2mAPhcz_AN2adMDYrxdDjukrVHctUTQifgjLRz5JvvQ";
            // var args9 = 267241698;
            // // script = start_hook()
            // // args = "android26724169807eb81a017fe33d51600741335863898565"
            // var args7 = "bd04cef92e993609b33d056df82a4380";
            var result = tt1.a(args1, args2, args3, args4, args5, args6, args7, args8, args9);
            ret['G-Auth-Sign'] = result.toString();
        });
        return ret
    }
};

