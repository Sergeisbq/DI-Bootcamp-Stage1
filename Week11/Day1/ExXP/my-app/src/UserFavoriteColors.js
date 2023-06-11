import React from 'react';

class UserFavoriteColors extends React.Component {
    render() {
        const {userinfo} = this.props;
        const {favAnimals} = userinfo;
        return (
            <>
                {
                    favAnimals.map((item, i) => {
                        return (
                            <div key={i}>
                                {item}
                            </div>
                        )
                    })
                }
            </>
        )
    }
}



export default UserFavoriteColors
