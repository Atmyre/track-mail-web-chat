var React = require('react');
var ReactDOM = require('react-dom');

var Cookies7 = Cookies.noConflict();
//Cookies2.set('csrftoken', 'X-CSRFToken');

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
            <div>
                <div>
                    <button className="button btn-group" onClick={() => this.props.onClick()}>
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
                                  'X-CSRFToken': 'MVOgcqA143wxWrOmGLfhFGU3irI2DdoyrRxHnfZ4diho46hnwSn1UurVRoNzzL42'
                              },
                              body: JSON.stringify({
                                message: message,
                                chat_id: item_pk,
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
            //window.alert(this.state.user_id);
            console.log(response);
            response.json().then(function (chats) {
                _this.setState({chats: chats});
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
            form = <div id="messages-table" className="row">
                        <div className="col-md-8">
                            <label htmlFor="id_send_message"></label>&nbsp;
                            <input
                                onChange={this.onChangeMessage.bind(this)}
                                id="id_send_message"
                                type="text"
                                size="100"
                                value={this.state.message}
                            />
                            <button onClick={() => this.sendMessage(this.state.chat_id, this.state.message)}>Send</button>
                        </div>
                    </div>
        }

        return (
            <div>
                <div>
                    <label htmlFor="id_search"></label>&nbsp;
                    <input
                        onChange={this.onChangeChats.bind(this)}
                        id="id_search"
                        type="text"
                        size="30"
                        value={this.state.content}
                    />
                    <button onClick={this.getChats.bind(this)}>Find</button>
                </div>
                <div className="row">
                    <div className="col-md-4">
                        {this.state.chats.map((item) => {
                            console.log(item.name);
                            return (<p key={item.pk}>
                                        <Chat value={item} onClick={() => this.handleClick(item.pk)}/>
                                    </p>)
                        })}
                    </div>
                    <div className="col-md-8">
                        {this.state.messages.map((item) => {
                            return (<p key={item.pk}>{item.text}</p>)
                        })}
                    </div>
                </div>

                {form}

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
