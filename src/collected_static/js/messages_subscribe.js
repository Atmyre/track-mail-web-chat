function subscribe_to_new_messages() {
  var $info = $('#messages-cent-data');
  var centrifuge = new Centrifuge({
    url: $info.data('cent-url'),
    user: $info.data('cent-user').toString(),
    timestamp: $info.data('cent-ts').toString(),
    info: $info.data('cent-info'),
    token: $info.data('cent-token'),
    debug: false,
  });

  var channel = $info.data('cent-channel');
  console.log('subscribe on channel ' + channel);
  centrifuge.subscribe(channel, function(msg) {
    console.log(msg);
    var row_html = '<tr><td>' + msg.data.text + '</td><td>' + 'frv' + '</td></tr>'
    $('#messages-table tr:last').after(row_html);
  });
  centrifuge.connect();
  return centrifuge;
}

var g_centrifuge = undefined;

$(document).ready(function() {
  g_centrifuge = subscribe_to_new_messages();
});