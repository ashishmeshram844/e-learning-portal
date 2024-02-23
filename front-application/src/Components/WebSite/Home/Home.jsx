import React, { Fragment } from 'react'
import SliderHome from './Slider/SliderHome'
import WebNavBar from '../WebsiteBase/WebNavBar'
import Footer from '../WebsiteBase/Footer'
const Home = () => {
  return (
    <Fragment>
      <WebNavBar />
      <SliderHome/>
      <Footer />
    </Fragment>
  )
}

export default Home