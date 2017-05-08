import React from "react"

export default class HomePageContainer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            courseTypes: [
            {name: "math",
            iconClassName: "pe-7s-display1"},
            {name: "science",
            iconClassName: "pe-7s-display1"},
            {name: "cpa",
            iconClassName: "pe-7s-display1"},
            {name: "cfa",
            iconClassName: "pe-7s-display1"},
            {name: "test1",
            iconClassName: "pe-7s-display1"},
            {name: "test2",
            iconClassName: "pe-7s-display1"},
            ],
            currCourseType: "math",
            courses: {
                "math": [
                    {name: "math Course 1", imgUrl: "https://www.w3schools.com/css/trolltunga.jpg", courseUrl: "http://google.com"},
                    {name: "math Course 2", imgUrl: "https://www.w3schools.com/css/trolltunga.jpg", courseUrl: "http://google.com"}
                ],
                "science": [],
                "cpa": [],
                "cfa": [],
                "test1": [],
                "test2": []
            }
        };
    }

    updateCourseType(courseTypeName) {
        this.setState({currCourseType: courseTypeName});
    }

    render() {
        let currCourseType = this.state.currCourseType;

        var courses = this.state.courses[currCourseType].map(function(course) {
            return (
                <div className="col-md-6">
                    <div className="client">
                    <p>{course.name}</p>
                    <a href={course.courseUrl}><img src={course.imgUrl} className="course-img"></img></a>
                    </div>
                </div>
            )
        })

        var courseTypes = this.state.courseTypes.map(function(courseType) {
            let typeClassStr = courseType.iconClassName + " icon-big";
            if (courseType.name == this.state.currCourseType) {
                typeClassStr += " active-course-type";
            }
            return (
                <div className="col-sm-2">
                    <a href="#a"><div className="team-member" onClick={this.updateCourseType.bind(this, courseType.name)}>
                        <i className={typeClassStr}></i>
                        <h5>{courseType.name}</h5>
                    </div></a>
                </div>                
            )
        }.bind(this));

        return (
            <div>
                <section id="subjects">
                    <div className="container">
                        <div className="row text-center">
                            <div className="col-md-6 col-md-offset-3">
                                <h1><span>SUBJECTS</span></h1>
                                <p>Click each subject to see which courses we offer.</p>
                                <hr />
                            </div>
                        </div>

                        <div className="row m-t-lg text-center">
                            {courseTypes}
                        </div>

                    </div>
                </section>


                <section id="courses" className="light-blue">

                    <div className="container">
                        <div className="row text-center m-t-lg">
                            <div className="col-md-12" id="course-panels">
                                {courses}
                            </div>
                        </div>
                    </div>
                </section>
            </div>
        )
    }
}
