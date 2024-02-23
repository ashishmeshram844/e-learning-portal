import React, { Fragment } from 'react'
import BannerInner from '../Banner/BannerInner'
import aboutImage from '../../../../assets/Image/aboutimage.jpg'
const About = () => {
  return (
    <Fragment>
      <BannerInner BgBackground={aboutImage} bgTitle={'About'}/>
    </Fragment>
  )
}

export default About