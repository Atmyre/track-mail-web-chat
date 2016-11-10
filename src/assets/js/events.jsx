var React = require('react');
var ReactDOM = require('react-dom');


class EventList extends React.Component {
    constructor() {
        super();
        this.state = {
            events: [],
        };
        this.getEvents.bind(this);
        this.getEvents();
    }

    getEvents() {

        let _this = this;
        fetch('/api/event/', {
            mode: "same-origin",
            credentials: "same-origin",
            method: 'get',
            cache: false
        })
        .then(function (response) {
            console.log(response);
            response.json().then(function (events) {
                _this.setState({events: events});
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
