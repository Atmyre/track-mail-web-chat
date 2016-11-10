var React = require('react');
var ReactDOM = require('react-dom');


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
                <button className="button btn-group" onClick={() => this.props.onClick()}>
                    {this.props.value.name }
                </button>
            </div>
        );
    }
}


class ChatList extends React.Component {
    constructor() {
        super();
        this.state = {
            chats: [],
            messages: [],
        };
        this.getChats.bind(this);
        this.getChats();
    }

    handleClick(item_pk) {
        let _this = this;
        fetch('/api/message/?chat_id=' + item_pk, {mode: "same-origin",
                            credentials: "same-origin",
                            method: 'get',
                            cache: false})
                .then(function (response) {
                    console.log(response);
                    response.json().then(function (messages) {
                        _this.setState({messages: messages});
                    })
                })
                .catch(function (err) {
                    console.log('Error:', err);
                })
    }

    getChats() {

        let _this = this;
        fetch('/api/chat/', {
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
        return (
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
