import React, { Fragment } from 'react'
import BannerInner from '../Banner/BannerInner'
import contactImage from '../../../../assets/Image/aboutimage.jpg'

const Contact = () => {
  return (
    <Fragment>
      <BannerInner BgBackground={contactImage} bgTitle={'Contact'}/>
    </Fragment>
  )
}

export default Contact