import React from "react"
import { render } from "react-dom"

import HomePageContainer from "./containers/HomePageContainer"

class HomePage extends React.Component {
  render() {
    return (
        <HomePageContainer />
    )
  }
}

render(<HomePage/>, document.getElementById('HomePage'))
