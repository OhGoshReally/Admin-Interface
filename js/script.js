

function ping(url, callback) {
  $.ajax({
    url: url,
    type: "HEAD",
    timeout:1000
  }).done(function() {
    callback(true);
  })
  .fail(function() {
    callback(false);
  })
};

function availability(status) {
  console.log(status)
}

function getLinks() {
  $("#links a").each( function () {
    ping(this.href, availability);
  })
}
