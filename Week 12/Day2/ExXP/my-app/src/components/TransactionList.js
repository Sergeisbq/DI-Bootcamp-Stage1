import React from 'react';
import { connect } from "react-redux";
import { insert_transaction, update_transaction, delete_transaction, update_current_id} from '../redux/actions';

const TransactionList = (props) => {

    const handleEdit = (item) => {
        props.infotransaction.
        // props.update_transaction1(item)
    }

    const handleDelete = (i) => {
        // e.preventDefault();
        console.log(i);
        // console.log(e.target.offsetParent.__reactFiber$wfcow630o1o.key);

        props.deleteTransaction1(i)
    }
    return (
        <>
        {props.list_transactions.length !== 0 &&
            props.list_transactions.map((item,i) => 
                <table key={i}>
                    <tbody key={i}>
                        <tr key={i}>
                            <td>{item.accountNumber}</td>
                            <td>{item.FSC}</td>
                            <td>{item.name}</td>
                            <td>{item.amount}</td>
                            <td><button onClick={() => handleEdit(item)}>EDIT</button></td>
                            <td><button onClick={() => handleDelete(i)}>DELETE</button></td>
                        </tr>
                    </tbody>
                </table>
            )
        }
        </>
    )
}

const mapStateToProps = (state) => {
    return {
        list_transactions: state.list 
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        updateTransactionIndex: (id) => dispatch(update_current_id(id)),
        deleteTransaction1: (id1) => {
            return (
                dispatch(delete_transaction(id1))
            )
        },
        // update_transaction1: (current_transaction) => dispatch(update_transaction(current_transaction))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(TransactionList)