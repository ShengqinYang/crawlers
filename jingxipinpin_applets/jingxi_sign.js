function getSignString(e) {
    e = JSON.parse(e);

    var t = orderByAscII(e),
        n = getParamsValue(t);
    return n = n.toString(), md5(n, "xtl_sqg_mall-^&*-damai_(789)_@#$")
}

function orderByAscII(e) {
    var t = [], n = 0;
    for (var a in e) t[n] = a, n++;
    var r = t.sort(), i = {};
    for (var o in r) i[r[o]] = e[r[o]];
    return i
}

function getParamsValue(e) {
    var t = "";
    for (var n in e) {
        var a = e[n];
        a instanceof Object && (a = JSON.stringify(a)), void 0 != a && null != a && ("number" == typeof a || "boolean" == typeof a || "" != a ? t += "&" + a : console.log("---key---,----value----", n, a))
    }
    return t = t.substring(1, t.length)
}


function md5(e, t, n) {
    function a(e, t) {
        var n = (65535 & e) + (65535 & t);
        return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
    }

    function r(e, t) {
        return e << t | e >>> 32 - t
    }

    function i(e, t, n, i, o, c) {
        return a(r(a(a(t, e), a(i, c)), o), n)
    }

    function o(e, t, n, a, r, o, c) {
        return i(t & n | ~t & a, e, t, r, o, c)
    }

    function c(e, t, n, a, r, o, c) {
        return i(t & a | n & ~a, e, t, r, o, c)
    }

    function s(e, t, n, a, r, o, c) {
        return i(t ^ n ^ a, e, t, r, o, c)
    }

    function u(e, t, n, a, r, o, c) {
        return i(n ^ (t | ~a), e, t, r, o, c)
    }

    function l(e, t) {
        var n, r, i, l, d;
        e[t >> 5] |= 128 << t % 32, e[14 + (t + 64 >>> 9 << 4)] = t;
        var p = 1732584193, f = -271733879, m = -1732584194, h = 271733878;
        for (n = 0; n < e.length; n += 16) r = p, i = f, l = m, d = h, f = u(f = u(f = u(f = u(f = s(f = s(f = s(f = s(f = c(f = c(f = c(f = c(f = o(f = o(f = o(f = o(f, m = o(m, h = o(h, p = o(p, f, m, h, e[n], 7, -680876936), f, m, e[n + 1], 12, -389564586), p, f, e[n + 2], 17, 606105819), h, p, e[n + 3], 22, -1044525330), m = o(m, h = o(h, p = o(p, f, m, h, e[n + 4], 7, -176418897), f, m, e[n + 5], 12, 1200080426), p, f, e[n + 6], 17, -1473231341), h, p, e[n + 7], 22, -45705983), m = o(m, h = o(h, p = o(p, f, m, h, e[n + 8], 7, 1770035416), f, m, e[n + 9], 12, -1958414417), p, f, e[n + 10], 17, -42063), h, p, e[n + 11], 22, -1990404162), m = o(m, h = o(h, p = o(p, f, m, h, e[n + 12], 7, 1804603682), f, m, e[n + 13], 12, -40341101), p, f, e[n + 14], 17, -1502002290), h, p, e[n + 15], 22, 1236535329), m = c(m, h = c(h, p = c(p, f, m, h, e[n + 1], 5, -165796510), f, m, e[n + 6], 9, -1069501632), p, f, e[n + 11], 14, 643717713), h, p, e[n], 20, -373897302), m = c(m, h = c(h, p = c(p, f, m, h, e[n + 5], 5, -701558691), f, m, e[n + 10], 9, 38016083), p, f, e[n + 15], 14, -660478335), h, p, e[n + 4], 20, -405537848), m = c(m, h = c(h, p = c(p, f, m, h, e[n + 9], 5, 568446438), f, m, e[n + 14], 9, -1019803690), p, f, e[n + 3], 14, -187363961), h, p, e[n + 8], 20, 1163531501), m = c(m, h = c(h, p = c(p, f, m, h, e[n + 13], 5, -1444681467), f, m, e[n + 2], 9, -51403784), p, f, e[n + 7], 14, 1735328473), h, p, e[n + 12], 20, -1926607734), m = s(m, h = s(h, p = s(p, f, m, h, e[n + 5], 4, -378558), f, m, e[n + 8], 11, -2022574463), p, f, e[n + 11], 16, 1839030562), h, p, e[n + 14], 23, -35309556), m = s(m, h = s(h, p = s(p, f, m, h, e[n + 1], 4, -1530992060), f, m, e[n + 4], 11, 1272893353), p, f, e[n + 7], 16, -155497632), h, p, e[n + 10], 23, -1094730640), m = s(m, h = s(h, p = s(p, f, m, h, e[n + 13], 4, 681279174), f, m, e[n], 11, -358537222), p, f, e[n + 3], 16, -722521979), h, p, e[n + 6], 23, 76029189), m = s(m, h = s(h, p = s(p, f, m, h, e[n + 9], 4, -640364487), f, m, e[n + 12], 11, -421815835), p, f, e[n + 15], 16, 530742520), h, p, e[n + 2], 23, -995338651), m = u(m, h = u(h, p = u(p, f, m, h, e[n], 6, -198630844), f, m, e[n + 7], 10, 1126891415), p, f, e[n + 14], 15, -1416354905), h, p, e[n + 5], 21, -57434055), m = u(m, h = u(h, p = u(p, f, m, h, e[n + 12], 6, 1700485571), f, m, e[n + 3], 10, -1894986606), p, f, e[n + 10], 15, -1051523), h, p, e[n + 1], 21, -2054922799), m = u(m, h = u(h, p = u(p, f, m, h, e[n + 8], 6, 1873313359), f, m, e[n + 15], 10, -30611744), p, f, e[n + 6], 15, -1560198380), h, p, e[n + 13], 21, 1309151649), m = u(m, h = u(h, p = u(p, f, m, h, e[n + 4], 6, -145523070), f, m, e[n + 11], 10, -1120210379), p, f, e[n + 2], 15, 718787259), h, p, e[n + 9], 21, -343485551), p = a(p, r), f = a(f, i), m = a(m, l), h = a(h, d);
        return [p, f, m, h]
    }

    function d(e) {
        var t, n = "", a = 32 * e.length;
        for (t = 0; t < a; t += 8) n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
        return n
    }

    function p(e) {
        var t, n = [];
        for (n[(e.length >> 2) - 1] = void 0, t = 0; t < n.length; t += 1) n[t] = 0;
        var a = 8 * e.length;
        for (t = 0; t < a; t += 8) n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
        return n
    }

    function f(e) {
        return d(l(p(e), 8 * e.length))
    }

    function m(e, t) {
        var n, a = p(e), r = [], i = [];
        for (r[15] = i[15] = void 0, a.length > 16 && (a = l(a, 8 * e.length)), n = 0; n < 16; n += 1) r[n] = 909522486 ^ a[n], i[n] = 1549556828 ^ a[n];
        var o = l(r.concat(p(t)), 512 + 8 * t.length);
        return d(l(i.concat(o), 640))
    }

    function h(e) {
        var t, n, a = "0123456789abcdef", r = "";
        for (n = 0; n < e.length; n += 1) t = e.charCodeAt(n), r += a.charAt(t >>> 4 & 15) + a.charAt(15 & t);
        return r
    }

    function g(e) {
        return unescape(encodeURIComponent(e))
    }

    function v(e) {
        return f(g(e))
    }

    function b(e) {
        return h(v(e))
    }

    function x(e, t) {
        return m(g(e), g(t))
    }

    function y(e, t) {
        return h(x(e, t))
    }

    function O() {
        return (65536 * (1 + Math.random()) | 0).toString(16).substring(1)
    }

    return t ? n ? x(t, e) : y(t, e) : n ? v(e) : b(e)
}

function jingxi_sign(body) {
    var sign_body = getSignString(JSON.stringify(body));
    console.log('sign_body', sign_body);
    return sign_body
}


// https://api.m.jd.com/jxpp.picksite.queryAddress?appid=jxpp_miniprogram&functionId=jxpp.picksite.queryAddress&t=1610013962152&body={"longitude":116.397849,"latitude":39.903776,"searchKey":"","cityName":"","queryType":2,"pageSize":10,"pageNo":1,"time":1610013962259,"signStr":"aa898735c4e1faae7bc64b6d2d4cc3af"}&channel=wxappjxpp&cv=1.1.0

// https://api.m.jd.com/jxpp.picksite.queryOpenCityList?appid=jxpp_miniprogram&functionId=jxpp.picksite.queryOpenCityList&body=body={"longitude":116.397849,"latitude":39.903776,"time":1610101416468,"signStr":"89fea70ebbef1405a9703da9580c1b4a"}
// Host: api.m.jd.com
// Accept: */*
// Content-Type: application/json
// Connection: keep-alive
// User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.13(0x17000d2a) NetType/WIFI Language/zh_CN
// Referer: https://servicewechat.com/wxf95d0d80e9d5bfc0/12/page-frame.html
// Accept-Language: zh-cn
// Accept-Encoding: br, gzip, deflate
