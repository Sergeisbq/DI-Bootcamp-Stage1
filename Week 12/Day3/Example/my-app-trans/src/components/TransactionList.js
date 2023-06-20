import TransactionForm from "./TransactionForm";
import {useSelector, useDispatch} from 'react-redux';
import { update_indx, delete_trx } from '../redux/actions';


const TransactionList = (props) => {
    const list = useSelector(state => state.list)

    const dispatch = useDispatch();


    return (
        <>
            <TransactionForm />
            <h2>Transaction List</h2>
            <table style={{border:"1px solid #ccc"}}><tbody>
                {
                    list.map((item,i) => {
                        return (
                            <tr key={i}>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    {item.accountNumber}
                                </td>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    {item.FSC}
                                </td>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    {item.name}
                                </td>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    {item.amount}
                                </td>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    <button onClick={() => dispatch(update_indx(i))}>EDIT</button>
                                </td>
                                <td style={{border:"1px solid #ccc", padding: '5px'}}>
                                    <button onClick={() => dispatch(delete_trx(i))}>DELETE</button>
                                </td>
                            </tr>
                        )
                    })
                }
            </tbody></table>
        </>
    )
}

export default TransactionList