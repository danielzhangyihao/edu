import React from "react"
import { render } from "react-dom"

import CoursesPageContainer from "./containers/CoursesPageContainer"

class CoursesPage extends React.Component {
  render() {
    return (
        <CoursesPageContainer />
    )
  }
}

render(<CoursesPage/>, document.getElementById('CoursesPage'))
