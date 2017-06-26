import React from "react"

export default class CoursesPageContainer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            displayType: "myCourses",
            filter: "All",
            myCourses: [],
            allCourses: [],
            query: "",
            loaded: false
        };
    }

    componentDidMount() {
        /*
        @TODO(yihao): Give me a backend endpoint that gives me list of json objects
        Data structure:
        { 
            'myCourses': [{
                'name': 'fakename', 
                'price': 80, 
                'numBought': 300, 
                'salesEndDate': '2017-05-12', 
                'numSpotsLeft': 20,
                'teacherName': 'cool guy'
            }],
            'allCourses': [{
                'name': 'fakename', 
                'price': 80, 
                'numBought': 300, 
                'salesEndDate': '2017-05-12', 
                'numSpotsLeft': 20,
                'teacherName': 'cool guy'
            }]
        }
        */

        // And then you can uncomment this code
        $.get("/education/get_courses/", function(result) {
            console.log('Resultss', result);
            //console.log('parsed results', JSON.parse(result.myCourses));
            this.setState({
                myCourses: result.myCourses,
                allCourses: result.allCourses,
                loaded: true
            })
        }.bind(this));
        
        
    }

    setFilter(filter) {
        this.setState({
            filter: filter
        })
    }

    setDisplayType(displayType) {
        this.setState({
            displayType: displayType
        })
    }

    updateQuery(event) {
        this.setState({
            query: event.target.value
        })
    }

    render() {
        let courseNodes;
        if (!this.state.loaded) {
            courseNodes = (
                <div className="text-center">
                    <div className="loader-1"></div>
                </div>
            )
        }
        console.log(this.state.loaded);
        console.log(this.state.displayType);
        console.log(this.state.myCourses);

        let coursesToRender = [];
        if (this.state.displayType == "myCourses") {
            coursesToRender = this.state.myCourses || [];
        } else if (this.state.displayType == "allCourses") {
            coursesToRender = this.state.allCourses || [];
        }

        if (coursesToRender.length == 0) {
            courseNodes = (
                <div className="hpanel">
                    <div className="panel-body">
                        <h3>No courses available!</h3>
                        <p>There does not seem to be any courses here.</p>
                    </div>
                </div>
            )
        } else {
            courseNodes = coursesToRender.map(function(course) {
                if (this.state.displayType == "myCourses") {
                    return (
                        <div className="col-sm-3">
                            <div className="hpanel contact-panel">
                                <a href="/course"><div className="panel-body">
                                    <img className="course-img" src="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera.s3.amazonaws.com/topics/ml/large-icon.png?auto=format%2Ccompress&dpr=1&fit=crop&w=225&h=130">
                                    </img>
                                    <hr />
                                    <h5 className="text-muted font-bold m-b-xs">{course.lesson_name} <small>(999 people bought this!)</small></h5>
                                    <p>Taught by: abc</p>
                                    <p>Class Start: May 5th</p>
                                </div></a>
                                <div className="panel-footer contact-footer text-center">
                                    <a href="/course"><button className="btn btn-primary">Go To Class</button></a>
                                </div>
                            </div>
                        </div>
                    )                    
                } else if (this.state.displayType == "allCourses") {
                    return (
                        <div className="col-sm-3">
                            <a href="#"><div className="hpanel contact-panel">
                                <div className="panel-body">
                                    <img className="course-img" src="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera.s3.amazonaws.com/topics/ml/large-icon.png?auto=format%2Ccompress&dpr=1&fit=crop&w=225&h=130">
                                    </img>
                                    <hr />
                                    <h5 className="text-muted font-bold m-b-xs">{course.lesson_name} <small>(999 people bought this!)</small></h5>
                                    <p>Taught by: abc</p>
                                    <p>Class Start: May 5th</p>
                                    <p><b>Spots Left: 200</b></p>

                                </div>
                                <div className="panel-footer contact-footer text-center">
                                    <button className="btn btn-success">BUY <small>(${course.price})</small></button>
                                </div>
                            </div></a>
                        </div>
                    )     
                }

            }.bind(this))    

            if (this.state.displayType == "myCourses") {
                courseNodes.push(
                    <div className="col-sm-3" >
                        <a href="#"><div className="hpanel contact-panel" onClick={this.setDisplayType.bind(this, "allCourses")}>
                            <div className="panel-body" style={{"height": "211px"}}>
                                <h5>Want to learn more?</h5>
                                <p>We have an enormous catalog of other great courses to learn from.</p>

                            </div>
                            <div className="panel-footer contact-footer text-center">
                                <button className="btn btn-success">SEE MORE COURSES</button>
                            </div>
                        </div></a>
                    </div>
                )                   
            }        
        }

        return (
        <div id="wrapper">
            <div className="content animate-panel">
                <div className="row">
                    <div className="col-sm-12">
                        <div className="dashboard-tab-container">

                            <a href="#a" className={this.state.displayType == "myCourses" ? "active-tab dashboard-tab" : "dashboard-tab"} onClick={this.setDisplayType.bind(this, "myCourses")}>
                                <div>
                                    My Courses
                                </div>
                            </a>
                            <a href="#a" className={this.state.displayType == "allCourses" ? "active-tab dashboard-tab" : "dashboard-tab"} onClick={this.setDisplayType.bind(this, "allCourses")}>
                                <div>
                                    Courses Catalog
                                </div>
                            </a>                                                                         
                        </div>
                    </div>
                </div>

                {/*
                This is some logic to enable querying by course type. 
                This might be useful later so I left code inline here as a comment.

                <div className="row">
                    <div className="col-lg-12">
                        <div className="hpanel">
                            <div className="panel-body">


                                <h2 className="font-light m-b-xs">
                                    Your Courses
                                </h2>
                                <small>These are the courses that you have already paid for.<br />You can go to these courses during the course time to see a live stream.</small>

                                <br /><br />
                                <div className="dropdown input-sm" style={ {"display": "inline"} }>
                                    <button className="btn btn-default dropdown-toggle" style={ { "padding": "4px 6px"} } type="button" id="menu1" data-toggle="dropdown">
                                    <span className="margin-right"><small>Currently Viewing: {this.state.filter} Classes</small></span>
                                    <span className="caret"></span></button>
                                    <ul className="dropdown-menu" role="menu" aria-labelledby="menu1">
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Math")}>Math</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Science")}>Science</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "CPA")}>CPA</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Math")}>Math</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Science")}>Science</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "CPA")}>CPA</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Math")}>Math</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "Science")}>Science</a></li>
                                        <li role="presentation"><a role="menuitem" href="#" onClick={this.setFilter.bind(this, "CPA")}>CPA</a></li>
                                  </ul>
                                </div>
                                <input className="form-control input-sm" style={ {"display": "inline", "width": "50%"} } type="text" placeholder="Search for class name.." value={this.state.query} onChange={this.updateQuery.bind(this)} />
                                

                            </div>
                        </div>

                    </div>
                </div>
                */}
                <div className="row">
                    <div className="col-lg-12">
                        {courseNodes}
                    </div>
                </div>
            </div>
        </div>

        )
    }
}
