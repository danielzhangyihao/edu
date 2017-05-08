

var CourseRenderer = React.createClass({
  getInitialState: function() {
  	return {
  		currentSubject: "Math"
  	}
  }

  render: function() {
    return (
		<div>
		    <section id="subjects">
		        <div className="container">
		            <div className="row text-center">
		                <div className="col-md-6 col-md-offset-3">
		                    <h1><span>SUBJECTS</h1>
		                    <p>Click each subject to see which courses we offer.</p>
		                    <hr />
		                </div>
		            </div>

		            <div className="row m-t-lg text-center">
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big" style="color:#ADD8E6"></i>
		                        <h5>Math</h5>
		                    </div></a>
		                </div>
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big"></i>
		                        <h5>Computer Science</h5>
		                    </div></a>
		                </div>
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big"></i>
		                        <h5>CPA</h5>
		                    </div></a>
		                </div>
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big"></i>
		                        <h5>CFA</h5>
		                    </div></a>
		                </div>
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big"></i>
		                        <h5><span>User</span> name</h5>
		                    </div></a>
		                </div>
		                <div className="col-sm-2">
		                    <a href="#a"><div className="team-member">
		                        <i className="pe-7s-display1 icon-big"></i>
		                        <h5><span>User</span> name</h5>
		                    </div></a>
		                </div>
		            </div>

		        </div>
		    </section>


		    <section id="courses" style="background-color:#ADD8E6">
		        <div className="container">
		            <div className="row text-center m-t-lg">
		                <div className="col-md-12">
		                    <div className="row">
		                        <div className="col-md-6">
		                            <div className="client" style={height:"240px"}>Course 1</div>
		                        </div>
		                        <div className="col-md-6">
		                            <div className="client" style={height:"240px"}>Course 2</div>
		                        </div>
		                    </div>
		                </div>
		            </div>
		        </div>
		    </section>
		</div>
    );
  }
});
