import React from 'react';

const PosLogin = () => {
    return(
        <main class="login">
      <div class="login__form">
      <h1>Hecho por Jeampier Cornejo</h1>
        <h1>Inicio de Sesión</h1>
        <form class="formulario">
          <label for="">Email:</label>
          <input type="email" class="formulario__input" placeholder="Email" />
          <label for="">Password:</label>
          <input
            type="password"
            class="formulario__input"
            placeholder="Password"
          />
          <button class="formulario__submit" type="submit">
            Iniciar Sesión
          </button>
        </form>
      </div>
    </main>
    );
};
export default PosLogin;

