import React, { Fragment } from 'react'
import BannerInner from '../Banner/BannerInner'
import organizerImage from '../../../../assets/Image/aboutimage.jpg'

const Organizer = () => {
  return (
    <Fragment>
      <BannerInner BgBackground={organizerImage} bgTitle={'Organizer'}/>
    </Fragment>
  )
}

export default Organizer