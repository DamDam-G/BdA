/*(function()
 {*/
var Iw =
{
    version: 1,
    author: 'Damien Goldenberg',
    xhr: {},
    excep:'ex',
    menu:
    {
        tar:'a',
        cls:'menu'
    },
    area:'display',
    context: '',
    lastX: '',
    lastY: '',
    hue: 0,
    kkeys: [],
    konami: "38,38,40,40,37,39,37,39,66,65",

    Init: function ()
    {
        $('.carousel').carousel({
            interval: 5000
        });
        Iw.CancelLink();
        Iw.xhr = Iw.Xhttpr();
        Iw.AttrDisplay();
        Iw.AttrArti();
        Iw.Calendar();
        Iw.AddEvent(window, "keydown", function(e)
        {
            Iw.kkeys.push(e.keyCode);
            if (Iw.kkeys.toString().indexOf(Iw.konami) >= 0)
            {
                if (document.getElementById("easteregg"))
                {
                    document.getElementById("easteregg").parentNode.removeChild(document.getElementById("easteregg"));
                }
                var tmp = document.body.appendChild(document.createElement("div"));
                tmp.id = "easteregg";
                document.getElementById("easteregg").innerHTML = '<canvas id="konami" width="700" height="350"></canvas>';
                Iw.context = document.getElementById("konami").getContext("2d");
                Iw.lastX = Iw.context.canvas.width * Math.random();
                Iw.lastY = Iw.context.canvas.height * Math.random();
                setInterval("Iw.AnimLine();", 50);
                setInterval("Iw.AnimBlank();", 40);
                Iw.kkeys = [];
            }
        });
        var audio = new Iw.Audio();
        Iw.AddEvent(document.getElementById("play"), 'click', audio.Play);
        Iw.AddEvent(document.getElementById("stop"), 'click', audio.Resume);
        document.getElementById('playlist').setAttribute('autoplay', 'true');
    },

    CancelLink: function ()
    {
        var oA = document.getElementsByTagName('a');

        for (var h = 0; h < oA.length; h++)
        {
            if (oA[h].className != Iw.excep)
            {
                oA[h].onclick = function()
                {
                    return false;
                };
            }
        }
    },

    AttrArti: function ()
    {
        var oA = document.getElementsByTagName('div');

        for (var h = 0; h < oA.length; h++)
        {
            if (/artc/.test(oA[h].className))
            {
                var tmp = new Iw.Display(oA[h].id);
                Iw.AddEvent(oA[h], 'click', tmp.arti);
            }
        }
    },

    AttrDisplay : function ()
    {
        var elements = document.getElementsByTagName(Iw.menu.tar);
        for(var i = 0; i < elements.length; i++)
        {
            if (elements[i].className == Iw.menu.cls)
            {
                var tmp = new Iw.Display(elements[i].id);
                Iw.AddEvent(elements[i], 'click', tmp.disp);
            }
        }
    },

    AttrCal : function ()
    {
        var elements = document.getElementsByTagName('td');
        for(var i = 0; i < elements.length; i++)
        {
            if (elements[i].className == 'event')
            {
                var tmp = new Iw.Display(elements[i].id);
                Iw.AddEvent(elements[i], 'click', tmp.disp);
            }
        }
    },

    Display : function(id)
    {
        this.id = id;
        this.disp = function()
        {
            Iw.xhr.onreadystatechange = function()
            {
                if (Iw.xhr.readyState == 4 && (Iw.xhr.status == 200 || Iw.xhr.status == 0))
                {
                    // Remplissage des données textuelles récupérées
                    document.getElementById(Iw.area).innerHTML = Iw.xhr.responseText;
                }
            };
            Iw.xhr.open("POST", "../controller/controller.php", true);
            Iw.xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // permet l'encodage des POST
            Iw.xhr.send("c="+this.id);
        };

        this.arti = function()
        {
            Iw.xhr.onreadystatechange = function()
            {
                if (Iw.xhr.readyState == 4 && (Iw.xhr.status == 200 || Iw.xhr.status == 0))
                {
                    // Remplissage des données textuelles récupérées
                    $('#article').modal('show');
                    document.getElementById("adisp").innerHTML = Iw.xhr.responseText;
                }
            };
            Iw.xhr.open("POST", "../view/article.php", true);
            Iw.xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // permet l'encodage des POST
            Iw.xhr.send("id="+this.id);
        };


    },

    Audio: function()
    {
        var player = document.getElementById("playlist");
        this.Play = function()
                    {
                        var control = document.getElementById("play");
                        if (player.paused)
                        {
                            player.play();
                            control.innerHTML = '<i class="icon-play"></i> Play';
                            control.className = "btn btn-success hidden-desktop";
                        }
                        else
                        {
                            player.pause();
                            control.innerHTML = '<i class="icon-pause"></i> Pause';
                            control.className = "btn btn-warning hidden-desktop";
                        }
                    };

        this.Resume = function()
                        {
                            player.currentTime = 0;
                            player.pause();
                        };
    },

    Calendar: function()
    {
        Iw.xhr.onreadystatechange = function()
        {
            if (Iw.xhr.readyState == 4 && (Iw.xhr.status == 200 || Iw.xhr.status == 0))
            {
                // Remplissage des données textuelles récupérées
                document.getElementById("calendar").innerHTML = Iw.xhr.responseText;
            }
        };
        Iw.xhr.open("POST", "../view/calendar.php", true);
        Iw.xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); // permet l'encodage des POST
        Iw.xhr.send();
    },

    AnimLine: function()
    {
        Iw.context.save();
        Iw.context.translate(Iw.context.canvas.width/2, Iw.context.canvas.height/2);
        Iw.context.scale(0.9, 0.9);
        Iw.context.translate(-Iw.context.canvas.width/2, -Iw.context.canvas.height/2);
        Iw.context.beginPath();
        Iw.context.lineWidth = 5 + Math.random() * 10;
        Iw.context.moveTo(Iw.lastX, Iw.lastY);
        Iw.lastX = Iw.context.canvas.width * Math.random();
        Iw.lastY = Iw.context.canvas.height * Math.random();
        Iw.context.bezierCurveTo(Iw.context.canvas.width * Math.random(), Iw.context.canvas.height * Math.random(), Iw.context.canvas.width * Math.random(), Iw.context.canvas.height * Math.random(), Iw.lastX, Iw.lastY);
        Iw.hue = Iw.hue + 10 * Math.random();
        Iw.context.strokeStyle = "hsl(" + Iw.hue + ", 50%, 50%)";
        Iw.context.shadowColor = "white";
        Iw.context.shadowBlur = 10;
        Iw.context.stroke();
        Iw.context.restore();
    },

    AnimBlank: function()
    {
        Iw.context.fillStyle = "rgba(0,0,0,0.1)";
        Iw.context.fillRect(0, 0, Iw.context.canvas.width, Iw.context.canvas.height);
    },

    Xhttpr :  function()
    {
        var xhr = null;
        if (window.XMLHttpRequest || window.ActiveXObject)
        {
            if (window.ActiveXObject)
            {
                try
                {
                    xhr = new ActiveXObject("Msxml2.XMLHTTP");
                }
                catch(e)
                {
                    xhr = new ActiveXObject("Microsoft.XMLHTTP");
                }
            }
            else
                xhr = new XMLHttpRequest();
        }
        else
        {
            alert("Votre navigateur ne supporte pas l'objet XMLHTTPRequest...");
            return null;
        }
        return xhr;
    },

    AddEvent: function (element, event, func)
    {
        if (element.attachEvent)
            element.attachEvent('on' + event, func);
        else
            element.addEventListener(event, func, true);
    }
};
Iw.AddEvent(window, 'load', Iw.Init());
// })();


