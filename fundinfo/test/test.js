function createMizToken() {
    function fmtNum(num) {
        return num > 9 ? num : "0" + num;
    }
    var now = new Date();
    var year = now.getFullYear();
    var month = fmtNum(now.getMonth() + 1);
    var day = fmtNum(now.getDate());
    var hour = fmtNum(now.getHours());
    var minute = fmtNum(now.getMinutes());
    var second = fmtNum(now.getSeconds());
    return (
        year +
        month +
        day +
        hour +
        minute +
        second +
        Math.random() +
        Math.random()
    );
}

// d=createMizToken()
// console.log(d)


e={
    "MaxMTLog": 300,
    "MTInterval": 4,
    "MinMTDwnLog": 30,
    "MaxKSLog": 14,
    "MaxFocusLog": 6,
    "MaxNGPLog": 200,
    "NGPInterval": 4,
    "Enable": 3,
    "location": "cn",
    "_umopt_npfp": 1,
    "timeout": 2000
}

function i(e, a, r, s, c, b, k) {
    for (var o = 12; void 0 !== o; ) {
        var t = 31 & o
          , n = o >> 5
          , h = 31 & n;
        switch (t) {
        case 0:
            !function() {
                switch (h) {
                case 0:
                    $ += "en",
                    o = 14;
                    break;
                case 1:
                    o = q < U.length ? 5 : 13;
                    break;
                case 2:
                    _ += "t",
                    o = 288;
                    break;
                case 3:
                    o = I ? 128 : 16;
                    break;
                case 4:
                    I += "Item",
                    o = 16;
                    break;
                case 5:
                    I += "et",
                    o = 96;
                    break;
                case 6:
                    q++,
                    o = 32;
                    break;
                case 7:
                    o = x < A.length ? 6 : 1;
                    break;
                case 8:
                    K += "PET",
                    o = 9;
                    break;
                case 9:
                    o = _ ? 33 : 65;
                    break;
                case 10:
                    g += "tch",
                    o = 15;
                    break;
                case 11:
                    x++,
                    o = 224;
                    break;
                case 12:
                    V++,
                    o = 512;
                    break;
                case 13:
                    P += "alSto",
                    o = 11;
                    break;
                case 14:
                    M += "l",
                    o = 3;
                    break;
                case 15:
                    _ += "d",
                    o = 4;
                    break;
                case 16:
                    o = V < B.length ? 2 : 7
                }
            }();
            break;
        case 1:
            !function() {
                switch (h) {
                case 0:
                    w[j](S),
                    o = void 0;
                    break;
                case 1:
                    _ += "ho",
                    o = 65;
                    break;
                case 2:
                    o = _ ? 480 : 4
                }
            }();
            break;
        case 2:
            var v = 753 ^ B.charCodeAt(V);
            W += String.fromCharCode(v),
            o = 384;
            break;
        case 3:
            return T[I](K, M),
            void 0;
        case 4:
            var p = "TSOP"
              , d = p.split("").reverse().join("");
            R[_] = d;
            var u = "ydob"
              , l = u.split("").reverse().join("");
            R[l] = r;
            var f = R
              , g = "fe";
            o = g ? 320 : 15;
            break;
        case 5:
            var C = 902 ^ U.charCodeAt(q);
            H += String.fromCharCode(C),
            o = 192;
            break;
        case 6:
            var m = 462 ^ A.charCodeAt(x);
            j += String.fromCharCode(m),
            o = 352;
            break;
        case 7:
            var w = N[W](z)
              , S = function(b) {
                var k = "gni";
                k += "rt",
                k && (k += "S"),
                k += "ot",
                k = k.split("").reverse().join("");
                var o = E[k]()
                  , t = "loc";
                t && (t += "al"),
                t += "Stora",
                t && (t += "g"),
                t += "e";
                var n = c[t]
                  , h = "g";
                h && (h += "e"),
                h += "tIt",
                h += "em";
                for (var v = "\u01ca\u01a5\u01d7\u01a3", p = "", d = 0, u = 0; u < v.length; u++) {
                    u || (d = 442);
                    var l = v.charCodeAt(u)
                      , f = l ^ d;
                    d = l,
                    p += String.fromCharCode(f)
                }
                var g = n[h](p)
                  , C = o === g;
                if (C) {
                    for (var m = "\u041e\u0421\u0415\u0413\u041e\u0405\u0426\u0421\u0424\u0413\u0419\u0417", w = "", S = 0; S < m.length; S++) {
                        var A = m.charCodeAt(S) - 946;
                        w += String.fromCharCode(A)
                    }
                    for (var j = c[w], x = "\u01c6\u01d1\u01d9\u01db\u01c2\u01d1\u01fd\u01c0\u01d1\u01d9", y = "", O = 0; O < x.length; O++) {
                        var R = 436 ^ x.charCodeAt(O);
                        y += String.fromCharCode(R)
                    }
                    var _ = "po";
                    _ && (_ += "rt"),
                    j[y](_)
                }
                var M = a + 1;
                i(e, M, r, s, c)
            }
              , A = "\u01ad\u01af\u01ba\u01ad\u01a6"
              , j = ""
              , x = 0;
            o = 224;
            break;
        case 8:
            var E = e[a]
              , y = "htt";
            y += "p:",
            y += "//127.",
            y += "0.0.1:";
            var O = y + E
              , R = {}
              , _ = "me";
            o = _ ? 64 : 288;
            break;
        case 9:
            var M = "fai";
            o = M ? 448 : 3;
            break;
        case 10:
            var P = "loc";
            o = P ? 416 : 11;
            break;
        case 11:
            P += "rage";
            var T = c[P]
              , I = "s";
            o = I ? 160 : 96;
            break;
        case 12:
            var D = e.length
              , L = a >= D;
            o = L ? 10 : 8;
            break;
        case 13:
            var N = G[H](J)
              , z = function(e) {
                var a = new TextDecoder
                  , r = "edoced"
                  , s = r.split("").reverse().join("")
                  , k = a[s](e)
                  , o = "par";
                o && (o += "se");
                var t = JSON[o](k)
                  , i = t;
                if (i) {
                    var n = "wwm"
                      , h = n.split("").reverse().join("");
                    i = t[h]
                }
                var v = i;
                if (v) {
                    var p = "mww";
                    b[63] = t[p]
                }
                var d = "l";
                d && (d += "oc"),
                d && (d += "alStor"),
                d && (d += "ag"),
                d += "e";
                for (var u = c[d], l = "\u016d\u0108\u017c\u0135\u0141\u0124\u0149", f = "", g = 0, C = 0; C < l.length; C++) {
                    C || (g = 286);
                    var m = l.charCodeAt(C)
                      , w = m ^ g;
                    g = m,
                    f += String.fromCharCode(w)
                }
                var S = "CP";
                S += "E",
                S += "T";
                for (var A = "\u03a3\u03a5\u03b3\u03b3\u03b5\u03a3\u03a3", j = "", x = 0; x < A.length; x++) {
                    var y = 976 ^ A.charCodeAt(x);
                    j += String.fromCharCode(y)
                }
                u[f](S, j);
                var O = "egarotSlacol"
                  , R = O.split("").reverse().join("")
                  , _ = c[R]
                  , M = "mw";
                M && (M += "w");
                var P = t[M]
                  , T = "met";
                T += "Ite",
                T += "s",
                T = T.split("").reverse().join("");
                for (var I = "\u01db\u01c1\u01c1", D = "", L = 0; L < I.length; L++) {
                    var N = 406 ^ I.charCodeAt(L);
                    D += String.fromCharCode(N)
                }
                _[T](D, P);
                var z = "loc";
                z += "al",
                z += "Stor",
                z += "a",
                z && (z += "ge");
                var B = c[z]
                  , W = "to";
                W += "S",
                W += "tr",
                W && (W += "ing");
                var V = E[W]()
                  , G = "set";
                G += "Item";
                var J = "trop"
                  , U = J.split("").reverse().join("");
                B[G](U, V)
            }
              , B = "\u0285\u0299\u0294\u029f"
              , W = ""
              , V = 0;
            o = 512;
            break;
        case 14:
            var G = X[$](Q)
              , J = function(e) {
                for (var a = atob(e), r = a.length, s = new ArrayBuffer(r), o = new Uint8Array(s), t = 0; t < a.length; t++)
                    o[t] = a.charCodeAt(t);
                var i = "cr";
                i && (i += "y"),
                i && (i += "p"),
                i && (i += "to");
                var n = c[i]
                  , h = "el";
                h && (h += "tb"),
                h && (h += "us"),
                h = h.split("").reverse().join("");
                for (var v = n[h], p = {}, d = "\xc4\x81\xd2\xff\xbc\xfe\xbd", u = "", l = 0, f = 0; f < d.length; f++) {
                    f || (l = 133);
                    var g = d.charCodeAt(f)
                      , C = g ^ l;
                    l = g,
                    u += String.fromCharCode(C)
                }
                p.name = u;
                var m = "vi"
                  , w = m.split("").reverse().join("");
                p[w] = k;
                for (var S = p, A = b[25], j = "nhcg", x = "", E = 0, y = 0; y < j.length; y++) {
                    y || (E = 10);
                    var O = j.charCodeAt(y)
                      , R = O ^ E;
                    E = O,
                    x += String.fromCharCode(R)
                }
                var _ = v[x](S, A, o);
                return _
            }
              , U = "\u03f2\u03ee\u03e3\u03e8"
              , H = ""
              , q = 0;
            o = 32;
            break;
        case 15:
            var X = c[g](O, f)
              , Q = function(e) {
                var a = "te";
                a && (a += "x"),
                a && (a += "t");
                var r = e[a]();
                return r
            }
              , $ = "th";
            o = $ ? 0 : 14;
            break;
        case 16:
            var K = "C";
            o = K ? 256 : 9
        }
    }
}


omsg=i(40,e)
console.log(omsg)