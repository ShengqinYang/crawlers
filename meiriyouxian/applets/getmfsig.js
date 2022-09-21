//

function func_n(e) {
    var g = 2048;

    function encodeUTF8(e, t) {
        var r = null;
        for ("number" == typeof e && (r = e, e = function () {
            return null
        }); null !== r || null !== (r = e());) 128 > r ? t(127 & r) : (2048 > r ? t(192 | 31 & r >> 6) : (65536 > r ? t(224 | 15 & r >> 12) : (t(240 | 7 & r >> 18), t(128 | 63 & r >> 12)), t(128 | 63 & r >> 6)), t(128 | 63 & r)), r = null
    }

    function UTF16toUTF8(e, t) {
        for (var r, o = null; null !== (r = null === o ? e() : o);) 55296 <= r && 57343 >= r && null !== (o = e()) && 56320 <= o && 57343 >= o ? (t(1024 * (r - 55296) + o - 56320 + 65536), o = null) : t(r);
        null !== o && t(o)
    }

    function encodeUTF16toUTF8(t, r) {
        UTF16toUTF8(t, function (t) {
            encodeUTF8(t, r)
        })
    }

    function n(e) {
        var t = Math.min(e.length, g), r = 0, o = [];
        return encodeUTF16toUTF8(function () {
            return r < t && o.length < g ? e.charCodeAt(r++) : null
        }, function (e) {
            o.push(e)
        }), o
    }

    return n(e)
}


function func_i(data, url) {
    var g = 2048;
    var y = function (e) {
        return func_n(e).slice(0, g).map(function (e) {
            return e.toString(16)
        }).join("")
    }

    function o(e) {
        var u = Math.ceil
        var _ = [".*?\\.missfresh\\.cn", ".*?\\.missfresh\\.net"]
        if (!_.some(function (t) {
            return new RegExp("^https?:\\/\\/" + t).test(e)
        })) {
            var t = "" + u(1e4 * Math.random());
            return "0".repeat(4 - t.length) + t
        }
        return ""
    }

    function i(n, url) {
        var r = {}
        var i, s = {};
        var u = n;
        var c = y(u);
        c && (s[c] = !0)
        return Object.keys(s).sort(function (e, t) {
            return e > t ? -1 : e < t ? 1 : 0
        }).join("") + o(url)
    }

    return i(data, url)
}

function MD5(e) {
    function a(e, t) {
        var r = (65535 & e) + (65535 & t);
        return (e >> 16) + (t >> 16) + (r >> 16) << 16 | 65535 & r
    }

    function i(e, t, r, o, n, i) {
        return a(function (e, t) {
            return e << t | e >>> 32 - t
        }(a(a(t, e), a(o, i)), n), r)
    }

    function s(e, t, r, o, n, a, s) {
        return i(t & r | ~t & o, e, t, n, a, s)
    }

    function u(e, t, r, o, n, a, s) {
        return i(t & o | r & ~o, e, t, n, a, s)
    }

    function c(e, t, r, o, n, a, s) {
        return i(t ^ r ^ o, e, t, n, a, s)
    }

    function d(e, t, r, o, n, a, s) {
        return i(r ^ (t | ~o), e, t, n, a, s)
    }

    function l(e, t) {
        var r, o, n, i, l;
        e[t >> 5] |= 128 << t % 32, e[14 + (t + 64 >>> 9 << 4)] = t;
        var p = 1732584193, h = -271733879, g = -1732584194, f = 271733878;
        for (r = 0; r < e.length; r += 16) h = d(h = d(h = d(h = d(h = c(h = c(h = c(h = c(h = u(h = u(h = u(h = u(h = s(h = s(h = s(h = s(n = h, g = s(i = g, f = s(l = f, p = s(o = p, h, g, f, e[r], 7, -680876936), h, g, e[r + 1], 12, -389564586), p, h, e[r + 2], 17, 606105819), f, p, e[r + 3], 22, -1044525330), g = s(g, f = s(f, p = s(p, h, g, f, e[r + 4], 7, -176418897), h, g, e[r + 5], 12, 1200080426), p, h, e[r + 6], 17, -1473231341), f, p, e[r + 7], 22, -45705983), g = s(g, f = s(f, p = s(p, h, g, f, e[r + 8], 7, 1770035416), h, g, e[r + 9], 12, -1958414417), p, h, e[r + 10], 17, -42063), f, p, e[r + 11], 22, -1990404162), g = s(g, f = s(f, p = s(p, h, g, f, e[r + 12], 7, 1804603682), h, g, e[r + 13], 12, -40341101), p, h, e[r + 14], 17, -1502002290), f, p, e[r + 15], 22, 1236535329), g = u(g, f = u(f, p = u(p, h, g, f, e[r + 1], 5, -165796510), h, g, e[r + 6], 9, -1069501632), p, h, e[r + 11], 14, 643717713), f, p, e[r], 20, -373897302), g = u(g, f = u(f, p = u(p, h, g, f, e[r + 5], 5, -701558691), h, g, e[r + 10], 9, 38016083), p, h, e[r + 15], 14, -660478335), f, p, e[r + 4], 20, -405537848), g = u(g, f = u(f, p = u(p, h, g, f, e[r + 9], 5, 568446438), h, g, e[r + 14], 9, -1019803690), p, h, e[r + 3], 14, -187363961), f, p, e[r + 8], 20, 1163531501), g = u(g, f = u(f, p = u(p, h, g, f, e[r + 13], 5, -1444681467), h, g, e[r + 2], 9, -51403784), p, h, e[r + 7], 14, 1735328473), f, p, e[r + 12], 20, -1926607734), g = c(g, f = c(f, p = c(p, h, g, f, e[r + 5], 4, -378558), h, g, e[r + 8], 11, -2022574463), p, h, e[r + 11], 16, 1839030562), f, p, e[r + 14], 23, -35309556), g = c(g, f = c(f, p = c(p, h, g, f, e[r + 1], 4, -1530992060), h, g, e[r + 4], 11, 1272893353), p, h, e[r + 7], 16, -155497632), f, p, e[r + 10], 23, -1094730640), g = c(g, f = c(f, p = c(p, h, g, f, e[r + 13], 4, 681279174), h, g, e[r], 11, -358537222), p, h, e[r + 3], 16, -722521979), f, p, e[r + 6], 23, 76029189), g = c(g, f = c(f, p = c(p, h, g, f, e[r + 9], 4, -640364487), h, g, e[r + 12], 11, -421815835), p, h, e[r + 15], 16, 530742520), f, p, e[r + 2], 23, -995338651), g = d(g, f = d(f, p = d(p, h, g, f, e[r], 6, -198630844), h, g, e[r + 7], 10, 1126891415), p, h, e[r + 14], 15, -1416354905), f, p, e[r + 5], 21, -57434055), g = d(g, f = d(f, p = d(p, h, g, f, e[r + 12], 6, 1700485571), h, g, e[r + 3], 10, -1894986606), p, h, e[r + 10], 15, -1051523), f, p, e[r + 1], 21, -2054922799), g = d(g, f = d(f, p = d(p, h, g, f, e[r + 8], 6, 1873313359), h, g, e[r + 15], 10, -30611744), p, h, e[r + 6], 15, -1560198380), f, p, e[r + 13], 21, 1309151649), g = d(g, f = d(f, p = d(p, h, g, f, e[r + 4], 6, -145523070), h, g, e[r + 11], 10, -1120210379), p, h, e[r + 2], 15, 718787259), f, p, e[r + 9], 21, -343485551), p = a(p, o), h = a(h, n), g = a(g, i), f = a(f, l);
        return [p, h, g, f]
    }

    function p(e) {
        var t, r = "", o = 32 * e.length;
        for (t = 0; t < o; t += 8) r += String.fromCharCode(255 & e[t >> 5] >>> t % 32);
        return r
    }

    function h(e) {
        var t, r = [];
        for (r[(e.length >> 2) - 1] = void 0, t = 0; t < r.length; t += 1) r[t] = 0;
        var o = 8 * e.length;
        for (t = 0; t < o; t += 8) r[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
        return r
    }

    function g(e) {
        var t, r, o = "0123456789abcdef", n = "";
        for (r = 0; r < e.length; r += 1) t = e.charCodeAt(r), n += o.charAt(15 & t >>> 4) + o.charAt(15 & t);
        return n
    }

    function f(e) {
        return unescape(encodeURIComponent(e))
    }

    function m(e) {
        return function (e) {
            return p(l(h(e), 8 * e.length))
        }(f(e))
    }

    function v(e, t) {
        return function (e, t) {
            var r, o, n = h(e), a = [], i = [];
            for (a[15] = i[15] = void 0, 16 < n.length && (n = l(n, 8 * e.length)), r = 0; 16 > r; r += 1) a[r] = 909522486 ^ n[r], i[r] = 1549556828 ^ n[r];
            return o = l(a.concat(h(t)), 512 + 8 * t.length), p(l(i.concat(o), 640))
        }(f(e), f(t))
    }

    function _(e, t, r) {
        return t ? r ? v(t, e) : function (e, t) {
            return g(v(e, t))
        }(t, e) : r ? m(e) : function (e) {
            return g(m(e))
        }(e)
    }

    return _(e)
}

function b(e) {
    return func_n(e).length
}

function a(e, t) {
    t = "0".repeat(4 - t.length) + t;
    var r = Array.prototype.map.call(t, function (e) {
        return e.charCodeAt(0)
    }), o = [];
    Array.prototype.forEach.call(e, function (t, n) {
        o.push((e.charCodeAt(n) + r[n % 4]) % 256)
    })
    return [].concat(o, r)
}

function Base64(e) {
    var _keyStr = "01234ABCDEFGHIJKLMNabcdefghijklmn+OPQRSTUVWXYZopqrstuvwxyz56789/=";

    function encode(e) {
        for (var t, r, o, n, a, i, s, u = "", c = 0; c < e.length;) n = (t = e[c++]) >> 2, a = (3 & t) << 4 | (r = e[c++]) >> 4, i = (15 & r) << 2 | (o = e[c++]) >> 6, s = 63 & o, u = isNaN(r) ? u + _keyStr.charAt(n) + _keyStr.charAt(a) : isNaN(o) ? u + _keyStr.charAt(n) + _keyStr.charAt(a) + _keyStr.charAt(i) : u + _keyStr.charAt(n) + _keyStr.charAt(a) + _keyStr.charAt(i) + _keyStr.charAt(s);
        return u
    }

    return encode(e)
}

function getmfsig(body, url) {
    var f = "01"
    var m = "00000d"
    var ts = Date.now()
    var llll = func_i(body, url)
    var arg1 = "ts=" + Math.ceil(ts / 1e4) + "&sign=" + MD5(llll + "/9ZBL0VjZovhR+Oiewgv20bb3He2L3IZ") + "&len=" + b(llll) + "&kv=" + m + "&av=" + f
    return Base64(a(arg1, "" + (ts % 1e4)))
}

// function getmfsig(request_body, url) {
//     var ts = Date.now()
//     var llll = func_i(request_body, url);
//     var sign = MD5(llll + "/9ZBL0VjZovhR+Oiewgv20bb3He2L3IZ")
//     var len = b(llll)
//     var arg1 = "ts=" + Math.ceil(ts / 1e4) + "&sign=" + sign + "&len=" + len + "&kv=" + m + "&av=" + f
//     var arg2 = ts % 1e4
//     var oooo = a(arg1, "" + arg2)
//     return Base64(oooo)
// }

// var request_body = '{"param":{"firstCategoryCode":"","secondCategoryCode":"","categoryIndex":0,"bizFingerprintType":3},"common":{"accessToken":"dlVYTmE1cTFCUEJEa2k1QmFlcUJHL2FXYzdoRDhKS0VpS2F5TUJCNGRXSU0xVytmSEdyK2d6M1BwZmJKWmhrTg==","retailType":"","fromSource":"","sourceDeviceId":"031cbae7-123d-8e49-857a-8d6f96c4772b","deviceId":"031cbae7-123d-8e49-857a-8d6f96c4772b","env":"weixin_app","platform":"weixin_app","model":"microsoft","screenHeight":736,"screenWidth":414,"version":"9.8.71.1","addressCode":110105,"stationCode":"MRYX|mryx_bjs_dxxrtd","bigWarehouse":"MRYXBJS","deliveryType":1,"chromeType":0,"currentLng":116.44355,"currentLat":39.921902,"sellerId":12159}}'
// var url = 'https://as-vip.missfresh.cn/as/home/classify'
// console.log(getmfsig(request_body, url))