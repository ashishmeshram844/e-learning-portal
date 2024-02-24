import React, { Fragment } from 'react'
import styles from './DashboardBase.module.css'
import { Link } from 'react-router-dom'

const BottomBar = () => {
  return (
    <Fragment>
        <div className={`${styles.BottomBarMain}`}>
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

export default BottomBar