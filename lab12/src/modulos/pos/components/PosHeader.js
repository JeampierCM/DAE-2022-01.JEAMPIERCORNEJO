import React from 'react';

const PosHeader = () => {
	return (
		<header className="header">
			<div className="header__logo">
				<img src="/img/logo.svg" alt="" />
			</div>
			<div className="header__buscador">
				<img src="/img/search.svg" alt="" />
				<input
					type="text"
					className="header__input"
					placeholder="Busca un término"
				/>
			</div>
			<div className="header__usuario">
				<img src="https://doriselisabustamante.files.wordpress.com/2010/06/perro-feliz.jpg" alt="" />
				<span>Jeampier Cornejo</span>
			</div>
		</header>
	);
};

export default PosHeader;
