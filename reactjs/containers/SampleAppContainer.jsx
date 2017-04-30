import React from "react"

import Headline from "../components/Headline"

export default class SampleAppContainer extends React.Component {
  render() {
    let {counters} = this.props
    return (
      <div className="container">
        <div className="row">
          <div className="col-sm-12">
            <Headline>Sample App1!</Headline>
          </div>
        </div>
      </div>
    )
  }
}
