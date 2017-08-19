import React, { Component } from 'react';
import Modal from 'react-modal';
import './App.css';

class App extends Component {
    constructor(){
        super();
        this.state = {
            isAddOpen: false,
            isTimeOpen: false,
            fetched_data: [{"time": '', "caption": ''}],
            time: '',
            caption: '',
            c: "run",
            t: '',
            ebent_time: [],
        };
    }

    openAdd(){
        this.setState({isAddOpen: true});
    }
    
    closeAdd(){
        this.setState({isAddOpen: false});
    }
    
    openTime(){
        this.setState({isTimeOpen: true});
    }
    
    closeTime(){
        this.setState({isTimeOpen: false});
    }
    
    componentDidMount(){
        var self = this;
        fetch("http://localhost:8000/events")
            .then(function(response){
                if (!response.ok){
                    console.log("error: bad response. status: " + response.status);
                }
                return response.json();
            })
            .then(function(response){
                self.setState({
                    fetched_data: response
                });
            })
    }
    
    componentWillMount(){
        this.createTime("8:00", "10:00", "0:20");
    }
    
    componentWillUpdate(){
        var self = this;
        fetch("http://localhost:8000/events")
            .then(function(response){
                if (!response.ok){
                    console.log("error: bad response. status: " + response.status);
                }
                return response.json();
            })
            .then(function(response){
                self.setState({fetched_data: response})
            })
    }
    
    onSubmit(e){
        e.preventDefault();
        fetch("http://localhost:8000/events", {
            method: "POST",
            body: JSON.stringify({"time": this.state.time, "caption": this.state.caption}),
            headers: {
                "Content-Type": "x-www-form-urlencoded",
            }
        });
        this.setState({isAddOpen:false})
    }
    
    onTimeClick(e, time, caption, self){
        fetch("http://localhost:8000/change_time",{
            method: "POST",
            body: JSON.stringify({"time": time.t, "caption": this.state.c}),
        });
        self.setState({isTimeOpen: false});
    }
    
    onTimeChange(e){
        this.setState({time: e.target.value})
    }
    
    onCaptionChange(e){
        this.setState({caption: e.target.value});
    }
    
    onRowClick(e, caption, self){
        self.setState({c: caption});
        self.setState({isTimeOpen: true});
    }
    
    onDelete(e, caption, time, self){
        self.setState({isTimeOpen: false});
        fetch("http://localhost:8000/delete", {
            method: "POST",
            body: JSON.stringify({"time": time, "caption": caption}),
        });
    }
    
    createTime(startTime, endTime, period, time){
        if (this.state !== []){
            var arr = [];
            startTime = startTime.split(':');
            var startTimeMin = parseInt(startTime[0])*60 + parseInt(startTime[1]);
            endTime = endTime.split(':');
            var endTimeMin = parseInt(endTime[0])*60 + parseInt(endTime[1]);
            period = period.split(':');
            var periodMin = parseInt(period[0])*60 + parseInt(period[1]);
            
            for (var i=startTimeMin; i<=endTimeMin; i+=periodMin){
                console.log(i);
                var str = parseInt(i / 60);
                str += ":";
                str += (i%60 !== 0) ? i%60:"00";
                arr.push(str)
            }
            
            this.setState({event_time:arr});
        }
    }
    
    deleteSecs(time){
        var time_arr = time.split(':');
        var t = time_arr[0]%10 > 0 ? time_arr[0][1]:time_arr[0];
        time = t + ":" + time_arr[1];
        return time;
    }
    
    render(){
        var c;
        var self = this;
        return (
            <div id="wrapper">
                {/*Заголовок*/}
                <div className="title">
                    <h2>Список Мероприятий</h2>
                </div>
                {/*Окно добавления нового мероприятия + кнопка открытия окна*/}
                <button className="button" onClick={this.openAdd.bind(this)}>Добавить позицию</button>
                <Modal
                    className="add"
                    isOpen={this.state.isAddOpen}
                    contentLabel="Add"
                    onRequestClose={this.closeAdd.bind(this)}
                >
                    <p className="add_item">Добавить событие</p>
                    <form method="post" onSubmit={this.onSubmit.bind(this)}>
                        <input className="add_item" type="text" placeholder="time" value={this.state.time}
                            onChange={this.onTimeChange.bind(this)}/>
                        <input className="add_item" type="text" placeholder="caption" 
                            value={this.state.caption}
                            onChange={this.onCaptionChange.bind(this)}/>
                        <input className="add_item" type="submit" value="Добавить событие"/>
                    </form>
                    <button className="add_item" onClick={this.closeAdd.bind(this)}>Close</button>
                </Modal>
                
                {/*Список мероприятий*/}
                <table className="list">
                    <thead>
                        <tr>
                            <th className="check"/>
                            <th>time</th>
                            <th>caption</th>
                            <th/>
                        </tr>
                    </thead>
                    <tbody>
                    {
                        this.state.fetched_data.map(function(e){
                            var caption = e.caption;
                            var time = self.deleteSecs(e.time);
                            return <tr key={caption} onClick={(ev) => 
                                    self.onRowClick(ev, caption, self)}>
                                <td className="check"><input type="checkbox"/></td>
                                <td className="cell">{time}</td>
                                <td className="cell">{e.caption}</td>
                                <td className="delete"><button onClick={(ev) => 
                                    self.onDelete(ev, caption, time, self)}>x
                                </button></td>
                            </tr>
                        })
                    }
                    </tbody>
                </table>
                {/*Блок времени*/}
                <Modal
                    className="time"
                    isOpen={this.state.isTimeOpen}
                    contentLabel="Time"
                    onRequestClose={this.closeTime.bind(this)}
                >
                    {this.state.event_time.map(function(t){
                        return <button key={t} onClick={(e) =>
                            self.onTimeClick(e, {t}, {c}, self)}>{t}</button>;
                    })}
                    <button onClick={this.closeTime.bind(this)}>Close</button>
                </Modal>
            </div>
        );
    }
}

export default App;