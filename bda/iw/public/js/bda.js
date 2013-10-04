$(window).load((function()
                {
                    var id; //contains the id of the current click in the menu
                    var csrftoken = GetCookie('csrftoken'); // this is the django secure token for ajx request
                    var kkeys = [];

                    function GetCookie(name)
                    {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '')
                        {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++)
                            {
                                var cookie = jQuery.trim(cookies[i]);
                                if (cookie.substring(0, name.length + 1) == (name + '='))
                                {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    }

                    function Article()
                    {
                        $(".artc").on("click", function(e)
                                                {
                                                    $.ajax({
                                                        type: 'post',
                                                        headers:
                                                        {
                                                            "X-CSRFToken": csrftoken
                                                        },
                                                        data:
                                                        {
                                                            id:this.id
                                                        },
                                                        url: '/article/',
                                                        success:function(data)
                                                                {
                                                                    $("#adisp").html(data);
                                                                    $("#article").modal("show");
                                                                },
                                                        error: function()
                                                                {
                                                                    alert('La requête n\'a pas abouti');
                                                                }
                                                    })
                                                });
                    }

                    $("a.menu").on("click", function()
                                               {
                                                   id = this.id
                                                   $.ajax({
                                                       type: 'post',
                                                       headers:
                                                        {
                                                            "X-CSRFToken": csrftoken
                                                        },
                                                       data:
                                                        {
                                                           id:this.id
                                                        },
                                                       url: '/control/',
                                                       success:function(data)
                                                               {
                                                                    $("#display").html(data);
                                                                   if (id == 0)
                                                                   {
                                                                        Article()
                                                                   }
                                                                   else if ((id == 17 || (id < 7 && id > 1) || (id < 13 && id > 7)) && id != null)
                                                                   {
                                                                       $("#followme").on("submit", function(e)
                                                                                                {
                                                                                                    e.preventDefault()
                                                                                                    $.ajax({
                                                                                                        type: 'post',
                                                                                                        headers:
                                                                                                        {
                                                                                                            "X-CSRFToken": csrftoken
                                                                                                        },
                                                                                                        data:$(this).serialize(),
                                                                                                        //data:'titi',
                                                                                                        url: '/follow/',
                                                                                                        success:function(data)
                                                                                                                {
                                                                                                                    $("#finfo").html(data)
                                                                                                                },
                                                                                                        error: function()
                                                                                                                {
                                                                                                                    alert('La requête n\'a pas abouti');
                                                                                                                }
                                                                                                    })
                                                                                                });
                                                                   }
                                                                   else if (id == 16)
                                                                   {
                                                                       $('#calendar').fullCalendar(
                                                                           {
                                                                               header: {left: 'prev,next today', center: 'title', right: 'month,agendaWeek,agendaDay'},
                                                                               editable:false,
                                                                               events:'/events/',
                                                                               eventClick: function(calEvent, jsEvent, view) {
                                                                                   //alert('Event: ' + calEvent.title+ ' '+calEvent.calendar);
                                                                                   //alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
                                                                                   //alert('View: ' + view.name);

                                                                                   // change the border color just for fun
                                                                                   $(this).css('border-color', 'red');
                                                                                  $("#adisp").html((calEvent.content).replace(/\n/g, "<br />"));
                                                                                    $("#article").modal("show");
                                                                               }
                                                                           });
                                                                   }
                                                               },
                                                       error: function()
                                                               {
                                                                   alert('La requête n\'a pas abouti');
                                                               }
                                                   })
                                               });

                    $(window).on("keydown", function(event)
                                            {
                                                kkeys.push( event.keyCode );
                                                if (kkeys.toString().indexOf("38,38,40,40,37,39,37,39,66,65") >= 0)
                                                {
                                                    effects = ["konami0", "konami1", "konami2", "konami3"];
                                                    t = $("audio, div, span, a, input, button, nav");
                                                    for (var i = 0; i< t.length; i++)
                                                    {
                                                        $(t[i]).addClass(effects[function()
                                                                                    {
                                                                                        var j = Math.round(Math.random()*10);
                                                                                        return j > 3 ? Math.round(j/3) : j;
                                                                                    }()]);
                                                    }
                                                }
                                            });

                    Article();
                })());