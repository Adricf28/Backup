// Crear un sistema que solo deje entrar en una fiesta a los mayores de edad y que a la primera persona que entre despues de las dos de la mañana entre gratis.

let timer = 0

const access = (a,t) => {
    if (a < 18) {
        return console.log('You cant get in kiddo');
    }
    if (a >= 18) {
        if ((t >= 2 && t < 7) && timer === 0) {
            timer++
            return console.log('Get in for free, you are the first to come in after 2 am ;D');
        } else {
            return console.log('You can get in but its 12$ maboi');
        } 
    }
}

access(15, 22)
access(13,4)
access(19, 23)
access(21, 6)
access(18,5)