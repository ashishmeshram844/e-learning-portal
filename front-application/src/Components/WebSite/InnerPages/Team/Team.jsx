import React, { Fragment } from 'react'
import BannerInner from '../Banner/BannerInner'
import teamImage from '../../../../assets/Image/aboutimage.jpg'

const Team = () => {
  return (
    <Fragment>
      <BannerInner BgBackground={teamImage} bgTitle={'Team'}/>
    </Fragment>
  )
}

export default Team