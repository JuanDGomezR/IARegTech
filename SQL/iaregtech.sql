-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-05-2025 a las 21:58:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `iaregtech`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `certificados`
--

CREATE TABLE `certificados` (
  `id` int(11) NOT NULL,
  `sistema_id` int(11) DEFAULT NULL,
  `nivel_aprobacion` enum('Aprobado','Condicionado','Rechazado') DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  `fecha_emision` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `certificados`
--

INSERT INTO `certificados` (`id`, `sistema_id`, `nivel_aprobacion`, `observaciones`, `fecha_emision`) VALUES
(1, 1, 'Condicionado', 'Sistema muy complejo, requiere revisión adicional.', '2025-05-23 19:07:40');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluaciones_eticas`
--

CREATE TABLE `evaluaciones_eticas` (
  `id` int(11) NOT NULL,
  `sistema_id` int(11) DEFAULT NULL,
  `criterio` varchar(100) DEFAULT NULL,
  `resultado` tinyint(1) DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `evaluaciones_eticas`
--

INSERT INTO `evaluaciones_eticas` (`id`, `sistema_id`, `criterio`, `resultado`, `observaciones`) VALUES
(1, 1, 'Transparencia', 1, 'Cumple adecuadamente.'),
(2, 1, 'Discriminacion', 1, 'Cumple adecuadamente.'),
(3, 1, 'ControlHumano', 0, 'Debe mejorarse para cumplir criterios éticos.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sistemas_ia`
--

CREATE TABLE `sistemas_ia` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `sector` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `nivel_complejidad` enum('Bajo','Medio','Alto') DEFAULT NULL,
  `uso_datos_personales` tinyint(1) DEFAULT NULL,
  `tipo_aprendizaje` enum('Supervisado','No Supervisado') DEFAULT NULL,
  `nivel_intervencion_humana` enum('Alta','Media','Baja') DEFAULT NULL,
  `riesgo` enum('Bajo','Medio','Alto') DEFAULT NULL,
  `estado_certificacion` enum('Aprobado','Condicionado','Rechazado') DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sistemas_ia`
--

INSERT INTO `sistemas_ia` (`id`, `nombre`, `sector`, `descripcion`, `nivel_complejidad`, `uso_datos_personales`, `tipo_aprendizaje`, `nivel_intervencion_humana`, `riesgo`, `estado_certificacion`, `fecha_creacion`) VALUES
(1, 'pruebita', 'Educación', 'Pruebita del sistema ', 'Alto', 0, 'Supervisado', 'Media', 'Medio', 'Condicionado', '2025-05-23 19:06:57');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `certificados`
--
ALTER TABLE `certificados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sistema_id` (`sistema_id`);

--
-- Indices de la tabla `evaluaciones_eticas`
--
ALTER TABLE `evaluaciones_eticas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sistema_id` (`sistema_id`);

--
-- Indices de la tabla `sistemas_ia`
--
ALTER TABLE `sistemas_ia`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `certificados`
--
ALTER TABLE `certificados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `evaluaciones_eticas`
--
ALTER TABLE `evaluaciones_eticas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `sistemas_ia`
--
ALTER TABLE `sistemas_ia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `certificados`
--
ALTER TABLE `certificados`
  ADD CONSTRAINT `certificados_ibfk_1` FOREIGN KEY (`sistema_id`) REFERENCES `sistemas_ia` (`id`) ON DELETE CASCADE;

--
-- Filtros para la tabla `evaluaciones_eticas`
--
ALTER TABLE `evaluaciones_eticas`
  ADD CONSTRAINT `evaluaciones_eticas_ibfk_1` FOREIGN KEY (`sistema_id`) REFERENCES `sistemas_ia` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
