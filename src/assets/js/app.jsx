var React = require('react')
var ReactDOM = require('react-dom')


var config = {
    container: document.getElementsByClassName('b-wall')[0]
};

class MessageList extends React.Component {
    state = {
        objects: [],
    };

    loadDataFromServer() {
        let _this = this;


        fetch('/api/срфе/')
            .then(function (response) {
                console.log(response);
                response.json().then(function (data) {
                    console.log(data);
                    _this.setState({objects: data});
                })
            })
            .catch(function (err) {
                console.log('Error:', err)
            })
    }

    render() {
        console.log(this.state);

        return (
            <div>
                <button onClick={this.loadDataFromServer.bind(this)}>Go</button>
                {this.state.objects.map((item) => {
                    return (<p key={item.pk}>{item.text}</p>)
                })}
            </div>
        )
    }
}



class Root extends React.Component {
    render() {
        return (
            <MessageList />
        )
    }
}



ReactDOM.render(
    <Root />,
    config.container
);