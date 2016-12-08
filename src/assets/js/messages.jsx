var React = require('react');
var ReactDOM = require('react-dom');

var Cookies7 = Cookies.noConflict();

class Chat extends React.Component {
    constructor() {
        super();
        this.state = {
            value: null,
        };
    }

    render () {
        console.log(this.props);
        return (
            <div className="btn-group-justified">
                <div className="btn-group">
                    <button type="button" className="btn btn-default" onClick={() => this.props.onClick()}>
                        {this.props.value.name }
                    </button>
                </div>
            </div>
        );
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

class ChatList extends React.Component {
    constructor() {
        super();
        this.state = {
            chats_dict: {},
            chats: [],
            messages: [],
            content: '',
            message: '',
            chat_id: -1,
        };
        this.getChats.bind(this);
        this.getChats();
    }

    handleClick(item_pk) {
        let _this = this;

        fetch('/api/message/?chat_id=' + item_pk, {
                            mode: "same-origin",
                            credentials: "same-origin",
                            method: 'get',
                            cache: false})
                .then(function (response) {
                    console.log(response);
                    response.json().then(function (messages) {
                        _this.setState({messages: messages, chat_id: item_pk});


                          var $info = $('#container');
                          var centrifuge = new Centrifuge({
                            url: $info.data('cent-url'),
                            user: $info.data('cent-user').toString(),
                            timestamp: $info.data('cent-ts').toString(),
                            info: $info.data('cent-info'),
                            token: $info.data('cent-token'),
                          });

                          var channel = _this.state.chats_dict[_this.state.chat_id].channel_name;
                          centrifuge.subscribe(channel, function(msg) {
                            messages = _this.state.messages;
                            messages.push(msg.data);
                            _this.setState({messages: messages});
                          });
                          centrifuge.connect();

                    })
                })
                .catch(function (err) {
                    console.log('Error:', err);
                })
    }

    sendMessage(item_pk, message) {

        let _this = this;
        // axios.post('/api/message/', {
        //   params: {message: message, chat_id: item_pk},
        //
        // })
        fetch('/api/message/', {
                            //mode: "same-origin",
                            method: 'POST',
                              headers: {
                                'Content-Type': 'application/json',
                                  'X-CSRFTOKEN': getCookie('csrftoken')
                              },
                              body: JSON.stringify({
                                text: message,
                                chat: item_pk,
                              }),
                            credentials: "same-origin",
                            cache: false})
                .then(function (response) {
                    _this.setState({message: ''});
                    console.log(response);
                })
                .catch(function (err) {
                    console.log('Error:', err);
                })
    }

    onChangeChats(e) {
        this.setState({content: e.target.value});
    }

    onChangeMessage(e) {
        this.setState({message: e.target.value});
    }

    getChats() {

        let _this = this;
        fetch('/api/chat/?name=' + this.state.content, {
            mode: "same-origin",
            credentials: "same-origin",
            method: 'get',
            cache: false
        })
        .then(function (response) {
            console.log(response);
            var chats_dict = {};
            response.json().then(function (chats) {
                {chats.map((item) => {
                    chats_dict[item.pk] = item;
                })}
                _this.setState({chats: chats, chats_dict: chats_dict});
            })
        })
        .catch(function (err) {
            console.log('Error:', err);
        })

    }

    render() {
        console.log(this.state.chats);
        let form = null;
        if (this.state.chat_id != -1) {

                form =
                    <div className="input-group">
                        <input type="text"
                            className="form-control"
                            onChange={this.onChangeMessage.bind(this)}
                            id="id_send_message"
                            value={this.state.message}
                            placeholder="Type your message"/>
                        <span className="input-group-addon" onClick={() => this.sendMessage(this.state.chat_id, this.state.message)}><span className="glyphicon glyphicon-send"></span></span>
                    </div>


        }

        return (
            <div className="row" id="chat-page">
                <div className="col-sm-3">
                    <div className="input-group" id="search-chat">
                        <input type="text"
                            className="form-control"
                            onChange={this.onChangeChats.bind(this)}
                            id="id_search"
                            placeholder="Search"
                            value={this.state.content}/>
                        <span className="input-group-addon" onClick={this.getChats.bind(this)}><span className="glyphicon glyphicon-search"></span></span>
                    </div>

                    {this.state.chats.map((item) => {
                        console.log(item.name);
                        return (<Chat value={item} onClick={() => this.handleClick(item.pk)}/>)
                    })}
                </div>

                <div className="col-sm-5 col-sm-offset-1">
                    <div id="messages-table" className="message-area">
                        <ul className="list-unstyled">
                            {this.state.messages.map((item) => {
                                return (
                                    <li className="message-body">
                                        <div className="chat-body1x">
                                            <p key={item.pk}>{item.text}</p>
                                        </div>
                                    </li>)
                            })}
                        </ul>
                    </div>

                    {form}
                </div>

            </div>
            );

    }

}


class View extends React.Component {

  render() {
    return (
      <div className="chat">
        <div className="chat-board">
          <ChatList />
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <View />,
  document.getElementById('container')
);
