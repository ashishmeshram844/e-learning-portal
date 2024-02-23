import React, { Fragment } from 'react'
import styles from './ChildCompo.module.css'
import { Link } from 'react-router-dom'

const BreadCrumbs = (props) => {
  return (
    <Fragment>
        <div className={styles.BreadCrumbsMain}>
          <div className={styles.BCTitle}>
            <span>{props.Title}</span>
          </div>
          <div className={styles.BreadCrumbMenu}>
              <Link data-td-content="Home" to={'/dashboard'} className={styles.BCHome}><i className='icon-home'></i></Link>
              <span className='text-sm'>Dashboard</span>
          </div>
        </div>
    </Fragment>
  )
}

export default BreadCrumbs