import React, { Fragment, useState } from "react";
import TableCompoTop from "./TableCompoTop";
import { TableHover, TableMain } from "./TableMain";
import TableCompoBottom from "./TableCompoBottom";

const TableCompo = (props) => {
    const {dataRows, checkboxRequired} = props;

    const handleSelectAll = (event) => {
        const dataValue = event.currentTarget.getAttribute('data-attr');
        const updatedValue = dataValue === 'false' ? 'true' : 'false';
        event.currentTarget.setAttribute('data-attr', updatedValue);
        const checkboxes = document.querySelectorAll("[data-value]");
        checkboxes.forEach((checkbox) => {
          checkbox.setAttribute('data-value', updatedValue);
        });
    };
    const handleSelectOne = (event) => {
        const select = document.querySelector("[data-attr]");
        const checkboxValue = event.currentTarget.getAttribute('data-value');
        const updatedValue = checkboxValue === 'false' ? 'true' : 'false';
        event.currentTarget.setAttribute('data-value', updatedValue);
        const allCheckFalse = document.querySelector("[data-value='false']");
        const allCheckTrue = document.querySelector("[data-value='true']");
        select.setAttribute('data-attr', allCheckTrue && allCheckFalse ? 'un' : allCheckTrue ? 'true' : 'false');
      };

     return (
        <Fragment>
        <TableCompoTop 
            // isCheckedAll={isCheckedAll} 
            handleSelectAll={handleSelectAll} 
        />

        <TableMain 
            dataRows={dataRows} 
            checkboxRequired={checkboxRequired}
            handleSelectOne={handleSelectOne}
        >
            <TableHover 
                Edit={true} 
                Delete={true}
                AddMember={true}
            />
        </TableMain>

        <TableCompoBottom />
        </Fragment>
    );
};

export default TableCompo;
