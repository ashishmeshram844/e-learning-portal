import React, { Fragment } from 'react'
import styles from './ChildCompo.module.css'

export const CardCompoBig = (props) => {
  const {children} = props
  return (
    <Fragment>
      <div className={styles.CardCompoBig}>
        {children}
      </div>
    </Fragment>
  )
}

