import React, { Fragment } from 'react'
import BannerInner from '../Banner/BannerInner'
import eventImage from '../../../../assets/Image/aboutimage.jpg'

const Event = () => {
  return (
    <Fragment>
      <BannerInner BgBackground={eventImage} bgTitle={'Event'}/>
    </Fragment>
  )
}

export default Event