import React, { Fragment } from 'react'
import styles from './Banner.module.css'
import WebNavBar from '../../WebsiteBase/WebNavBar'
const BannerInner = ({BgBackground, bgTitle}) => {
  return (
    <Fragment>
        <WebNavBar />
        <div className={styles.BgBanner} style={{backgroundImage: `url(${BgBackground})`}}>
          <div className={styles.BannerTitleBg}>
            <h1 className={styles.BannerTitle}>{bgTitle}</h1>
          </div>
        </div>
    </Fragment>
  )
}

export default BannerInner