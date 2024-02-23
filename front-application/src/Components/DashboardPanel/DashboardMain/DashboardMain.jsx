import React, { Fragment } from 'react'
import { CardCompoBig } from '../ChildComponents/CardCompo'
import BreadCrumbs from '../ChildComponents/BreadCrumbs'
import TableCompo from '../ChildComponents/TableComponent/TableCompo'
const DashbaordMain = () => {
  const TableConetnt = [
    ['Apple MacBook',	'Silver',	'Laptop',	'$2999'],
    ['Microsoft Surface',	'White',	'Laptop PC'	,'$1999'],
    ['Magic Mouse',	'Black',	'Accessories',	'$99'],
    ['Google Pixel',	'Gray',	'Phone',	'$799'],
    ['Apple Watch',	'Red',	'Wearables',	'$999'],
  ]    
  return (
    <Fragment>
      <BreadCrumbs Title={'Dashboard'}/>
      <CardCompoBig>
        <TableCompo 
          dataRows={TableConetnt}
          checkboxRequired={true}
        />
      </CardCompoBig>  
    </Fragment>
  )
}


export default DashbaordMain