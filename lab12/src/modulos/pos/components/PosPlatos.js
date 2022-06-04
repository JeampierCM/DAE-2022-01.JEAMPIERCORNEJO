import React from 'react';
import PosPlato from './PosPlato';


const PosPlatos = ({objCategoria}) => {

	
	
	const platos = [
		{
			id: 1,
			nombre: "CAUSA LIMEÑA",
			imagen: "http://res.cloudinary.com/dd9ad40qm/image/upload/v1630162164/xvhka1e8uqzliedzem71.jpg",
			precio: 10.00
		},
		{
			id: 2,
			nombre: "PAPA RELLENA",
			imagen: "http://res.cloudinary.com/dd9ad40qm/image/upload/v1630170241/bvatccnvqpheclhaa1rl.jpg",
			precio: 15.00
		},
		{
			id: 3,
			nombre: "ARROS CHAUFA",
			imagen: "https://comidasperuanas.net/wp-content/uploads/2016/11/Arroz-chaufa.jpg",
			precio: 12.00
		}
		,
		{
			id: 4,
			nombre: "CEVICHE",
			imagen: "https://micevichedehoy.com/wp-content/uploads/2018/10/ceviche-carretillero_700x467-697x465.jpg",
			precio: 18.00
		}
	]

	return (
		<div className="carta">
			<h3>
				Lista de Platos Categoria: &nbsp;{' '}
				<span className="color-secundario">{objCategoria ? objCategoria.nombre : "Seleccione Categoria"}</span>
			</h3>

			<div className="carta__platos">
				{platos.map((objPlato) => {
					return <PosPlato objPlato={objPlato} key={objPlato.plato_id} />;
				})}
			</div>
		</div>
	);
};

export default PosPlatos;
