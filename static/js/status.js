function sabstatus() {
  url = $('#sab_url').val();
  key = $('#sab_key').val();
  console.log(url);
  console.log(key);

  url += "api?mode=queue&output=json&apikey=" + key

  console.log(url);

  $('#load').show();
  output = $.ajax({
    url: url,
    type: "HEAD",
    dataType: 'jsonp',
    timeout:1000
  })

  output.always(function (){
    $('#load').hide();
  });

  output.done(function (data) {
    console.log("Done");
    console.log(data);

    queue = data["queue"];

    $('#sab_queue').text(queue['noofslots']);
    $('#sab_timeLeft').text(queue['timeleft']);
    $('#sab_speed').text(queue['speed']);
    $('#sab_sizeTotal').text(queue['size']);
    $('#sab_sizeLeft').text(queue['sizeleft']);

    console.log("Output set");
  });

  output.fail(function (data) {
    console.log("Failed");
    console.log(data);
  });



}

function saveSab() {
  url = $('#sab_url').val();
  key = $('#sab_key').val();
  if(url != null) {
    localStorage.setItem("sab_url", url);
  }
  if(key != null) {
    localStorage.setItem("sab_key", key);
  }
}

function loadLocal() {
  sab_url = localStorage.getItem("sab_url");
  sab_key = localStorage.getItem("sab_key");
  if(sab_url != null) {
    $('#sab_url').val(sab_url);
  }
  if(sab_key != null) {
    $('#sab_key').val(sab_key);
  }
}

function loadComplete() {
  $('#load').ajaxStart(function() {
    $( this ).show();
  });
  $('#load').ajaxStop(function() {
    $( this ).hide();
  });

  loadLocal();

}
