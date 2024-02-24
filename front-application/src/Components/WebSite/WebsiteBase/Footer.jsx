import React, { Fragment } from 'react'
import styles from './WebsiteBase.module.css'
import { Link } from 'react-router-dom'
const Footer = () => {
  return (
    <Fragment>
        <div className={`${styles.FooterMain}`}>
          <span>Powered By </span>
          <Link target='_blank' to={'/'}>
              Test
          </Link>
          <span>&</span>
          <Link target='_blank' to={'/'}>
              Test
          </Link>
        </div>
    </Fragment>
  )
}

export default Footer